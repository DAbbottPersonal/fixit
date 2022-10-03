"""
This script will run a suite of common code clean-up utilities
"""

import logging
import subprocess
from pathlib import Path
from typing import Union

FORMAT = "%(asctime)s %(message)s"
logging.basicConfig(format=FORMAT)
logger = logging.getLogger("dafixup")


def _run_cmd(
    pkg_to_run: str,
    pkg_desc: str = "",
    path: Union[str, Path] = ".",
) -> None:
    """
    Command to run a package.
    """

    path = path.absolute() if isinstance(path, Path) else Path(path).absolute()
    cmd = [
        pkg_to_run,
        str(path),
    ]
    cmd_str = " ".join(cmd)
    logger.warning(f"Start %s: %s", pkg_desc, cmd_str)
    subprocess.call(cmd, shell=True)
    logger.warning(f"Finish %s", pkg_desc)


def run_import_sort(sort_path: Union[str, Path] = ".") -> None:
    """
    Run the import sorter.
    """

    _run_cmd(
        "isort",
        "Import Sorter",
        sort_path,
    )


def run_lint(lint_path: Union[str, Path] = ".") -> None:
    """
    Run the linter.
    """

    _run_cmd(
        "black",
        "Linter",
        lint_path,
    )


def run_all() -> None:
    """
    Run all the clean-up tools in sequence.
    """

    run_import_sort()
    run_lint()
