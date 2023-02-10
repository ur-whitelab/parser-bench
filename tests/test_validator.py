import os

from parser_bench.validator import validate_directory

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
example_dir = os.path.join(_THIS_DIR, "test_files", "zeopp-sa")


def test_integration_dir_validation():
    assert validate_directory(example_dir)
