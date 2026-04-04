#!/usr/bin/env python3
from __future__ import annotations

from functools import lru_cache
from pathlib import Path


BOOK_EXTENSIONS = {
    ".azw",
    ".azw3",
    ".djvu",
    ".epub",
    ".mobi",
    ".pdf",
}
IGNORE_NAMES = {
    ".git",
    ".github",
    "__pycache__",
    "scripts",
}
START_MARKER = "<!-- file-tree:start -->"
END_MARKER = "<!-- file-tree:end -->"

REPO_ROOT = Path(__file__).resolve().parents[1]
README_PATH = REPO_ROOT / "README.md"


def is_book_file(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in BOOK_EXTENSIONS


@lru_cache(maxsize=None)
def directory_has_books(directory: Path) -> bool:
    for entry in directory.iterdir():
        if should_ignore(entry):
            continue
        if is_book_file(entry):
            return True
        if entry.is_dir() and directory_has_books(entry):
            return True
    return False


def should_ignore(path: Path) -> bool:
    return path.name.startswith(".") or path.name in IGNORE_NAMES


def included_entries(directory: Path) -> list[Path]:
    directories: list[Path] = []
    files: list[Path] = []

    for entry in sorted(directory.iterdir(), key=lambda item: item.name.lower()):
        if should_ignore(entry):
            continue
        if entry.is_dir() and directory_has_books(entry):
            directories.append(entry)
        elif is_book_file(entry):
            files.append(entry)

    return directories + files


def render_tree(root: Path) -> str:
    lines = [f"{root.name}/"]

    def walk(directory: Path, prefix: str) -> None:
        entries = included_entries(directory)
        for index, entry in enumerate(entries):
            is_last = index == len(entries) - 1
            connector = "└── " if is_last else "├── "
            suffix = "/" if entry.is_dir() else ""
            lines.append(f"{prefix}{connector}{entry.name}{suffix}")
            if entry.is_dir():
                child_prefix = f"{prefix}{'    ' if is_last else '│   '}"
                walk(entry, child_prefix)

    walk(root, "")
    return "\n".join(lines)


def update_readme() -> None:
    readme = README_PATH.read_text()
    if START_MARKER not in readme or END_MARKER not in readme:
        raise RuntimeError("README.md is missing tree markers.")

    start_index = readme.index(START_MARKER) + len(START_MARKER)
    end_index = readme.index(END_MARKER)
    tree_block = f"\n```text\n{render_tree(REPO_ROOT)}\n```\n"
    updated = f"{readme[:start_index]}{tree_block}{readme[end_index:]}"
    README_PATH.write_text(updated)


if __name__ == "__main__":
    update_readme()
