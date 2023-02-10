import fire

from .validator import validate_directories


def _validate_directories(dir):
    out = validate_directories(dir)
    if out:
        return "✅ Validation passed"


def validate_dirs_cli():
    fire.Fire(_validate_directories)
