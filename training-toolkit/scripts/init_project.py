import argparse
import uuid
from pathlib import Path
from common import TOOLKIT, link_project, write_json

def initialize(project, name):
    project = project.resolve()
    if not name.strip() or '\n' in name or '\r' in name:
        raise ValueError('Display name must be one nonempty line')
    if project.exists():
        raise ValueError('Project path already exists; refusing overwrite')
    manifest = __import__('json').loads((TOOLKIT / 'manifest.json').read_text(encoding='utf-8'))
    project.mkdir(parents=True)
    for folder in ['programs/versions', 'programs/drafts', 'logs', 'changes', 'exports']:
        (project / folder).mkdir(parents=True)
    project_id = uuid.uuid4().hex
    for file in ['profile.md', 'roadmap.md', 'skill-candidates.md']:
        text = (TOOLKIT / 'templates' / file).read_text(encoding='utf-8')
        (project / file).write_text(text.replace('{{NAME}}', name).replace('{{PROJECT_ID}}', project_id), encoding='utf-8')
    state = dict(schema_version=1, project_id=project_id, toolkit_version=manifest['version'],
                 active_program=None, active_revision=None, pending_program=None, pending_revision=None,
                 latest_checkin=None, next_checkin=None, temporary_changes=[], exports=[])
    write_json(project / 'state.json', state)
    (project / 'current-state.md').write_text(
        '# Trạng thái hiện tại\n\n- Active program: none\n- Active revision: none\n'
        '- Pending program: none\n- Pending revision: none\n'
        '- Latest check-in: none\n- Next check-in: none\n\n'
        'Chưa có chương trình. Bắt đầu intake; chưa có dữ liệu thực tế hoặc chẩn đoán.\n'
        'Đồng bộ các dòng chỉ mục trên với state.json khi cập nhật.\n', encoding='utf-8')
    (project / 'exercise-links.md').write_text(
        '# Link bài đã kiểm tra\n\n| Bài/biến thể | URL | Nguồn | Ngày kiểm tra | Phạm vi/ghi chú |\n'
        '|---|---|---|---|---|\n\nChưa có link đã xác minh cho project. Không đoán URL.\n', encoding='utf-8')
    link_project(project, TOOLKIT, initial=True)
    return project

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a new isolated training project (never overwrite).')
    parser.add_argument('--project', type=Path, required=True)
    parser.add_argument('--name', required=True)
    args = parser.parse_args()
    try:
        print(initialize(args.project, args.name))
    except (ValueError, OSError) as exc:
        parser.exit(1, str(exc) + '\n')
