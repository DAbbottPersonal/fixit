#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dafixup Package Installation Unit Tests
"""

from filecmp import cmp
from pathlib import Path
from shutil import copy as cp
from xmlrpc.client import Boolean

from dafixup import run_typechecking

from .fixtures import (typechecked_test_python_file,
                       untypechecked_test_python_file)


def check_typechecked(p: Path) -> Boolean:
    o = run_typechecking(p)
    if "Found 1 error in 1 file" in o:
        return False
    return True


def test_import_sorter(untypechecked_test_python_file, typechecked_test_python_file):
    l = typechecked_test_python_file
    ul = untypechecked_test_python_file
    assert check_typechecked(l)
    assert not check_typechecked(ul)
