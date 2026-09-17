import argparse
from pathlib import Path
from common import link_project

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Relink an existing project; preserve pinned version and data.')
    parser.add_argument('--project', type=Path, required=True)
    parser.add_argument('--toolkit', type=Path, required=True)
    args = parser.parse_args()
    if not (args.project / 'state.json').is_file() or not (args.project / 'toolkit.json').is_file():
        parser.exit(1, 'Not an existing toolkit project\n')
    try:
        link_project(args.project.resolve(), args.toolkit.resolve())
        print('Relinked; personal data and pinned version preserved.')
    except (ValueError, OSError) as exc:
        parser.exit(1, str(exc) + '\n')
