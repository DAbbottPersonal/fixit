#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dafixup Package Installation Unit Tests
"""

from filecmp import cmp
from shutil import copy as cp

from dafixup import run_lint

from .fixtures import linted_test_python_file, unlinted_test_python_file


def test_linter(tmp_path, unlinted_test_python_file, linted_test_python_file):
    l = linted_test_python_file
    ul = tmp_path / "test_linter.py"
    cp(unlinted_test_python_file, ul)
    run_lint(ul)
    assert cmp(l, ul)
