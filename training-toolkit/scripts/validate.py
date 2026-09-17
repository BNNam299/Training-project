import argparse
import hashlib
import json
import re
from datetime import date
from pathlib import Path
from common import TOOLKIT, local_path, metadata

def validate_project(project):
    errors = []
    def fail(message): errors.append(message)
    try:
        root = project.resolve()
        for file in ['profile.md', 'roadmap.md', 'current-state.md', 'skill-candidates.md', 'exercise-links.md', 'AGENTS.md', 'CLAUDE.md']:
            if not (root / file).is_file(): fail('Missing ' + file)
        state = json.loads((root / 'state.json').read_text(encoding='utf-8'))
        config = json.loads((root / 'toolkit.json').read_text(encoding='utf-8'))
        toolkit = (root / config['toolkit_path']).resolve()
        release = json.loads((toolkit / 'manifest.json').read_text(encoding='utf-8'))
        if config['pinned_version'] != release['version']:
            fail('Toolkit version differs from project pin; review migration')
        if state['toolkit_version'] != config['pinned_version']:
            fail('state toolkit version differs from pin')
        for key in ['latest_checkin', 'next_checkin']:
            if state[key] is not None: date.fromisoformat(state[key])
        current = (root / 'current-state.md').read_text(encoding='utf-8')
        for label, key in [('Active program','active_program'),('Active revision','active_revision'),
                           ('Pending program','pending_program'),('Pending revision','pending_revision'),
                           ('Latest check-in','latest_checkin'),('Next check-in','next_checkin')]:
            value = 'none' if state[key] is None else str(state[key])
            if f'- {label}: {value}' not in current.splitlines():
                fail('current-state disagrees: ' + key)
        for mode in ['active','pending']:
            path, revision = state[mode + '_program'], state[mode + '_revision']
            if (path is None) != (revision is None): fail(mode + ' path/revision must both be null or set')
            if path is not None:
                meta = metadata(local_path(root, path))
                if type(revision) is not int or revision < 1: fail('Invalid revision')
                if meta['revision'] != revision: fail(mode + ' revision mismatch')
                allowed = ['active'] if mode == 'active' else ['draft','approved']
                if meta['status'] not in allowed: fail(mode + ' has incompatible status')
                if not meta.get('program_id'): fail('Missing program_id')
        if state['active_program'] and state['pending_program'] == state['active_program']:
            fail('Pending file must not overwrite active file')
        for change in state['temporary_changes']:
            if not local_path(root, change['file']).is_file(): fail('Missing change file')
            start = date.fromisoformat(change['starts_on'])
            if change['ends_on'] is not None and date.fromisoformat(change['ends_on']) < start:
                fail('Change ends before it starts')
            if not change['return_condition']: fail('Missing return condition')
        for export in state['exports']:
            if not local_path(root, export['file']).is_file(): fail('Missing export file')
            local_path(root, export['program'])
            if export['status'] not in ['current','stale']: fail('Invalid export status')
            if export['status'] == 'current' and (export['program'] != state['active_program'] or export['revision'] != state['active_revision']):
                fail('Outdated export marked current')
    except (KeyError, ValueError, TypeError, OSError) as exc:
        fail(str(exc))
    return errors

def validate_bundle():
    errors = []
    manifest = json.loads((TOOLKIT / 'manifest.json').read_text(encoding='utf-8'))
    for item in manifest['source_files']:
        p = local_path(TOOLKIT, item['path'])
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != item['sha256']:
            errors.append('Source integrity mismatch: ' + item['path'])
    if hashlib.sha256((TOOLKIT / 'knowledge.md').read_bytes()).hexdigest() != manifest['knowledge_sha256']:
        errors.append('Knowledge hash differs from manifest')
    for path in TOOLKIT.rglob('*.md'):
        relative = path.relative_to(TOOLKIT)
        if relative.parts[0] in ['references', '.tests']: continue  # Immutable source can contain legacy formatting.
        text = path.read_text(encoding='utf-8')
        if '\ufffd' in text: errors.append('Encoding replacement: ' + str(relative))
        for link in re.findall(r'\]\(([^)]+)\)', text):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:|#|/', link): continue
            target = link.split('#')[0]
            if not (path.parent / target).is_file(): errors.append(f'Broken link in {relative}: {link}')
    for skill in (TOOLKIT / 'skills').glob('*/SKILL.md'):
        text = skill.read_text(encoding='utf-8')
        if not text.startswith('---\n') or '\nname: ' not in text or '\ndescription: ' not in text:
            errors.append('Invalid skill frontmatter: ' + str(skill))
    return errors

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check package integrity or project state; not a clinical validator.')
    parser.add_argument('--project', type=Path)
    args = parser.parse_args()
    errors = validate_project(args.project) if args.project else validate_bundle()
    for error in errors: print('ERROR:', error)
    print(f'Validation: {len(errors)} error(s)')
    raise SystemExit(bool(errors))
