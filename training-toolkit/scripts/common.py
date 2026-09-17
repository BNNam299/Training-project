"""Local-only helpers; no network or third-party dependencies."""
import json
import os
import re
from pathlib import Path

TOOLKIT = Path(__file__).resolve().parents[1]

def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def local_path(root, value):
    if not isinstance(value, str) or not value or Path(value).is_absolute():
        raise ValueError('Expected nonempty relative project path')
    target = (root / value).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError('Path escapes project: ' + value)
    return target

def metadata(path):
    body = path.read_text(encoding='utf-8')
    match = re.search(r'```json\s*\n(.*?)\n```', body, re.S)
    if not match:
        raise ValueError('Missing program JSON metadata: ' + str(path))
    return json.loads(match.group(1))

def link_project(project, toolkit, initial=False):
    if not (toolkit / 'AGENTS.md').is_file() or not (toolkit / 'manifest.json').is_file():
        raise ValueError('Not a packaged toolkit')
    try:
        relative = Path(os.path.relpath(toolkit, project)).as_posix()
    except ValueError:
        relative = toolkit.as_posix()  # Different Windows drives: relink after transfer.
    config_path = project / 'toolkit.json'
    config = {} if initial else json.loads(config_path.read_text(encoding='utf-8'))
    config['toolkit_path'] = relative
    if initial:
        config['pinned_version'] = json.loads((toolkit / 'manifest.json').read_text(encoding='utf-8'))['version']
    write_json(config_path, config)
    entry = ('# Personal Training Project\n\n'
             'Đọc `toolkit.json`, resolve `toolkit_path` tương đối với thư mục này, rồi đọc AGENTS.md tại toolkit. '
             'So pinned_version với version toolkit; nếu lệch, xem thay đổi trước khi áp dụng kiến thức mới.\n\n'
             'Đọc current-state.md và state.json, profile.md, roadmap.md, chương trình active cùng log/change liên quan. '
             'Nếu chỉ mục mâu thuẫn, làm rõ/khôi phục trước khi ghi. Không dùng chương trình của project khác.\n')
    (project / 'AGENTS.md').write_text(entry, encoding='utf-8')
    (project / 'CLAUDE.md').write_text('# Claude\n\nĐọc AGENTS.md tại project này trước khi làm việc.\n', encoding='utf-8')
