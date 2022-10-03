#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dafixup Package Installation Unit Tests
"""

from filecmp import cmp
from shutil import copy as cp

from dafixup import run_import_sort

from .fixtures import sorted_test_python_file, unsorted_test_python_file


def test_import_sorter(tmp_path, unsorted_test_python_file, sorted_test_python_file):
    l = sorted_test_python_file
    ul = tmp_path / "test_import_sorter.py"
    cp(unsorted_test_python_file, ul)
    run_import_sort(ul)
    assert cmp(l, ul)
