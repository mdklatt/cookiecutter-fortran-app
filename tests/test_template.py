""" Test the Cookiecutter template.

A template project is created in a temporary directory, the application and its
test suite are built, and the test suite is executed.

"""
from json import loads
from pathlib import Path
from shlex import split
from subprocess import check_call
from tempfile import TemporaryDirectory

from cookiecutter.main import cookiecutter


def main() -> int:
    """ Execute the test.
    
    """
    template = Path(__file__).resolve().parents[1]
    defaults = loads(template.joinpath("cookiecutter.json").read_text())
    with TemporaryDirectory() as tmpdir:
        cookiecutter(str(template), no_input=True, output_dir=tmpdir)
        name = defaults["project_slug"]
        cwd = Path(tmpdir) / name
        for args in "-DCMAKE_BUILD_TYPE=Debug", "--build":
            check_call(split(f"cmake {args:s} ."), cwd=cwd)
        check_call(split(f"./{name:s} -h"), cwd=cwd)  # TODO: run test suite
    return 0
    
    
# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
