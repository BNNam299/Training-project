"""Build a portable ZIP from the toolkit without caches or recursive releases."""
import argparse
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {'.git', '.tests', '__pycache__', 'distribution'}


def build(output: Path) -> tuple[Path, int]:
    output = output.resolve()
    if output.exists():
        raise ValueError(f'Output already exists: {output}')
    output.parent.mkdir(parents=True, exist_ok=True)
    files = [
        path for path in sorted(ROOT.rglob('*'))
        if path.is_file() and not any(part in SKIP_PARTS for part in path.relative_to(ROOT).parts)
    ]
    with zipfile.ZipFile(output, 'x', zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, (Path(ROOT.name) / path.relative_to(ROOT)).as_posix())
    with zipfile.ZipFile(output) as archive:
        broken = archive.testzip()
        if broken:
            raise ValueError(f'ZIP verification failed at {broken}')
        if f'{ROOT.name}/manifest.json' not in archive.namelist():
            raise ValueError('ZIP is missing manifest.json')
    return output, len(files)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Build a portable toolkit ZIP; refuses overwrite.')
    manifest = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))
    parser.add_argument(
        '--output', type=Path,
        default=ROOT / 'distribution' / f'training-toolkit-v{manifest["version"]}.zip'
    )
    args = parser.parse_args()
    try:
        path, count = build(args.output)
        print(f'ZIP verified: {path} ({count} files, {path.stat().st_size} bytes)')
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        parser.exit(1, str(exc) + '\n')
