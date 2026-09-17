import argparse
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from common import local_path, metadata

def snapshot(project, program):
    source = local_path(project, program)
    meta = metadata(source)
    raw = source.read_bytes()
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    # Filename derives from actual file, not potentially untrusted metadata.
    destination = local_path(project, 'programs/versions')
    destination.mkdir(parents=True, exist_ok=True)
    target = destination / (source.stem + '-' + stamp + '-' + hashlib.sha256(raw).hexdigest()[:10] + '.md')
    with target.open('xb') as stream:
        stream.write(raw)
    return target

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Preserve exact program bytes before revision.')
    parser.add_argument('--project', type=Path, required=True)
    parser.add_argument('--program', required=True)
    args = parser.parse_args()
    try:
        print(snapshot(args.project.resolve(), args.program))
    except (ValueError, OSError) as exc:
        parser.exit(1, str(exc) + '\n')
