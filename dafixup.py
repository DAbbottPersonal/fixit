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


def run_lint(lint_path: Union[str, Path] = ".") -> None:
    """
    Run all the linter.
    """

    lint_path = (
        lint_path.absolute()
        if isinstance(lint_path, Path)
        else Path(lint_path).absolute()
    )
    cmd = [
        "black",
        str(lint_path),
    ]
    cmd_str = " ".join(cmd)
    logger.warning(f"Start Linter: %s", cmd_str)
    subprocess.call(cmd, shell=True)
    logger.warning(f"Finish Linter: %s", cmd_str)


def run_all() -> None:
    """
    Run all the clean-up tools in sequence.
    """

    run_lint()
