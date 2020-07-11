import os
import argparse
from pathlib import Path
from typing import List, Generator

STYLE = """
  section {
    font-size: 100%;
  }"""
MARP_HEADER = ["---\n", "marp: true\n", "style: |" + STYLE]


def get_all_files(directory: str) -> Generator:
    result = []
    for root, _, files in os.walk(directory):
        result.extend(os.path.join(root, f) for f in files)
    yield from sorted(result)

def get_md_files(directory: str) -> List[Path]:
    files = (Path(p) for p in get_all_files(directory))
    md_files = list(f for f in files if f.suffix.lower() == ".md")
    return md_files


def compile_to_one_text(files: List[Path]) -> Generator:
    yield from MARP_HEADER
    for file in files:
        with file.open("r") as inp:
            yield "\n\n---\n\n"
            yield from inp


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", help="Выходной файл", type=argparse.FileType("w"), default="_compiled_text.md")
    parser.add_argument("directory", help="Директория с .md файлами")
    return parser.parse_args()


def main(argv):
    files = get_md_files(argv.directory)
    compiled_lines = compile_to_one_text(files)
    with argv.output as out:
        out.writelines(compiled_lines)


if __name__ == "__main__":
    args = parse_args()
    main(args)
