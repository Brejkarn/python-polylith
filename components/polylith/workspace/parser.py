from pathlib import Path

import tomlkit
from polylith import repo


def _load_workspace_config(path: Path) -> tomlkit.TOMLDocument:
    fullpath = path / repo.workspace_file

    content = fullpath.read_text()

    return tomlkit.loads(content)


def get_namespace_from_config(path: Path) -> str:
    toml: dict = _load_workspace_config(path)

    return toml["tool"]["polylith"]["namespace"]


def get_git_tag_pattern_from_config(path: Path) -> str:
    toml: dict = _load_workspace_config(path)

    return toml["tool"]["polylith"]["git_tag_pattern"]


def is_test_generation_enabled(path: Path) -> bool:
    toml: dict = _load_workspace_config(path)

    enabled = toml["tool"]["polylith"]["test"]["enabled"]
    return bool(enabled)


def get_theme_from_config(path: Path) -> str:
    toml: dict = _load_workspace_config(path)

    return toml["tool"]["polylith"]["structure"]["theme"] or "tdd"


def get_brick_structure_from_config(path: Path) -> str:
    theme = get_theme_from_config(path)

    if theme == "loose":
        return "{brick}/{namespace}/{package}"

    return "{brick}/{package}/src/{namespace}/{package}"


def get_tests_structure_from_config(path: Path) -> str:
    theme = get_theme_from_config(path)

    if theme == "loose":
        return "test/{brick}/{namespace}/{package}"

    return "{brick}/{package}/test/{namespace}/{package}"
