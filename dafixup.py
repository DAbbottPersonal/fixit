"""
This script will run a suite of common code clean-up utilities
"""

import logging
import subprocess
from pathlib import Path
from sys import stdout
from typing import List, Union

FORMAT = "%(asctime)s %(message)s"
logging.basicConfig(format=FORMAT)
logger = logging.getLogger("dafixup")


def path_abs(path: Union[str, Path]) -> Path:
    """
    Return an absolute path from a str or Path.
    """

    p = path if isinstance(path, Path) else Path(path)
    return p.absolute()


def _run_cmd(
    pkg_to_run: str,
    pkg_options: List[str] = None,
    pkg_desc: str = "",
    path: Union[str, Path] = ".",
) -> str:
    """
    Command to run a package.
    """

    path = path_abs(path)
    cmd = pkg_options if pkg_options else []
    cmd.insert(0, pkg_to_run)
    cmd.append(str(path))

    cmd_str = " ".join(cmd)
    logger.warning("Start %s: %s", pkg_desc, cmd_str)
    std_out = subprocess.run(cmd, shell=True, capture_output=True)
    logger.warning(
        "Finish %s with output and error: \n%s\n%s",
        pkg_desc,
        std_out.stdout.decode(),
        std_out.stderr.decode(),
    )
    return std_out.stdout.decode()


def run_import_sort(sort_path: Union[str, Path] = ".") -> str:
    """
    Run the import sorter.
    """

    return _run_cmd(
        pkg_to_run="isort",
        pkg_desc="Import Sorter",
        path=sort_path,
    )


def run_lint(lint_path: Union[str, Path] = ".") -> str:
    """
    Run the linter.
    """

    return _run_cmd(
        pkg_to_run="black",
        pkg_desc="Linter",
        path=lint_path,
    )


def run_requirement_generation(req_path: Union[str, Path] = ".") -> str:
    """
    Run the code to make requirements.txt.
    """

    req_path = path_abs(req_path)
    return _run_cmd(
        pkg_to_run="pigar",
        pkg_options=[
            "-y",
            "-p",
            str(req_path / "requirements.txt"),
            "-P",
        ],
        pkg_desc="Requirement Generation",
        path=req_path,
    )


def run_typechecking(typecheck_path: Union[str, Path] = ".") -> str:
    """
    Run the typechecker.
    """

    return _run_cmd(
        pkg_to_run="mypy",
        pkg_options=[
            "--explicit-package-bases",
            "--namespace-packages",
        ],
        pkg_desc="Typechecking",
        path=typecheck_path,
    )


def run_all() -> None:
    """
    Run all the clean-up tools in sequence.
    """

    run_import_sort()
    run_lint()
    run_requirement_generation()
    run_typechecking()
