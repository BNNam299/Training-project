import json
import tempfile
import unittest
from pathlib import Path
from common import TOOLKIT, local_path, write_json, link_project
from init_project import initialize
from snapshot_program import snapshot
from validate import validate_project

class ProjectTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.project = initialize(Path(self.temp.name) / 'person', 'Người thử nghiệm')
    def tearDown(self):
        self.temp.cleanup()
    def state(self):
        return json.loads((self.project / 'state.json').read_text(encoding='utf-8'))
    def save(self, state):
        write_json(self.project / 'state.json', state)
        labels = [('Active program','active_program'),('Active revision','active_revision'),
                  ('Pending program','pending_program'),('Pending revision','pending_revision'),
                  ('Latest check-in','latest_checkin'),('Next check-in','next_checkin')]
        (self.project / 'current-state.md').write_text('# Trạng thái\n\n' + '\n'.join(
            f'- {label}: {state[key] if state[key] is not None else "none"}' for label,key in labels), encoding='utf-8')
    def active(self):
        p = self.project / 'programs/program-001.md'
        p.write_text('# Chương trình\n\n```json\n' + json.dumps(dict(program_id='program-001', revision=1, status='active')) + '\n```\n\nLịch sử r1\n', encoding='utf-8')
        state = self.state(); state.update(active_program='programs/program-001.md', active_revision=1)
        self.save(state)
        return p
    def test_new_isolated_projects_and_no_overwrite(self):
        self.assertEqual(validate_project(self.project), [])
        other = initialize(Path(self.temp.name) / 'other', 'Người khác')
        self.assertNotEqual(self.state()['project_id'], json.loads((other/'state.json').read_text())['project_id'])
        original = (self.project/'profile.md').read_bytes()
        with self.assertRaises(ValueError): initialize(self.project, 'Ghi đè')
        self.assertEqual(original, (self.project/'profile.md').read_bytes())
    def test_snapshot_preserves_exact_original(self):
        p = self.active(); raw = p.read_bytes()
        copied = snapshot(self.project, 'programs/program-001.md')
        p.write_text('Đã thay đổi', encoding='utf-8')
        self.assertEqual(copied.read_bytes(), raw)
    def test_escape_rejected_without_copy(self):
        with self.assertRaises(ValueError): local_path(self.project, '../outside.md')
        with self.assertRaises(ValueError): snapshot(self.project, '../outside.md')
        state=self.state(); state.update(active_program='../outside.md', active_revision=1);self.save(state)
        self.assertTrue(any('escapes' in e for e in validate_project(self.project)))
    def test_revision_and_pointer_mismatch_detected(self):
        self.active(); self.assertEqual(validate_project(self.project), [])
        state=self.state();state['active_revision']=2;self.save(state)
        self.assertTrue(any('revision mismatch' in e for e in validate_project(self.project)))
        (self.project/'current-state.md').write_text('# Cũ', encoding='utf-8')
        self.assertTrue(any('current-state disagrees' in e for e in validate_project(self.project)))
    def test_pending_cannot_replace_active(self):
        self.active();state=self.state();state.update(pending_program=state['active_program'],pending_revision=1);self.save(state)
        self.assertTrue(any('overwrite active' in e for e in validate_project(self.project)))
    def test_stale_export_detected(self):
        self.active(); (self.project/'exports/example.docx').write_bytes(b'test placeholder, not a Word artifact')
        state=self.state();state['exports']=[dict(file='exports/example.docx',program='programs/program-001.md',revision=0,status='current')];self.save(state)
        self.assertTrue(any('Outdated export' in e for e in validate_project(self.project)))
        state['exports'][0]['status']='stale';self.save(state)
        self.assertEqual(validate_project(self.project), [])
    def test_relink_preserves_profile_state_and_pin(self):
        before={name:(self.project/name).read_bytes() for name in ['profile.md','state.json']}
        old=json.loads((self.project/'toolkit.json').read_text())
        moved=self.project.with_name('moved');self.project.rename(moved);self.project=moved
        link_project(moved,TOOLKIT)
        for name,raw in before.items():self.assertEqual(raw,(moved/name).read_bytes())
        self.assertEqual(old['pinned_version'],json.loads((moved/'toolkit.json').read_text())['pinned_version'])
        self.assertEqual(validate_project(moved), [])
    def test_temporary_change_requires_valid_range(self):
        (self.project/'changes/c1.md').write_text('Đổi tạm',encoding='utf-8')
        state=self.state();state['temporary_changes']=[dict(id='c1',file='changes/c1.md',starts_on='2026-09-15',ends_on='2026-09-14',status='active',return_condition='Review')];self.save(state)
        self.assertTrue(any('ends before' in e for e in validate_project(self.project)))

if __name__ == '__main__': unittest.main()
