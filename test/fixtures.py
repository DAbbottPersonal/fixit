#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fixtures for Unit Tests
"""
import pytest


@pytest.fixture
def unsorted_test_python_file(tmp_path):
    d = tmp_path / "import"
    d.mkdir(exist_ok=True)
    p = d / "unsorted.py"
    p.write_text(
        """
import pillow
import abcdefg
import numpy
import pandas
"""
    )
    return p


@pytest.fixture
def sorted_test_python_file(tmp_path):
    d = tmp_path / "import"
    d.mkdir(exist_ok=True)
    p = d / "sorted.py"
    p.write_text(
        """
import abcdefg
import numpy
import pandas
import pillow
"""
    )
    return p


@pytest.fixture
def unlinted_test_python_file(tmp_path):
    d = tmp_path / "lint"
    d.mkdir(exist_ok=True)
    p = d / "unlinted.py"
    p.write_text(
        """
import pandas
fake_test_string = 'this is an absurdly long line' if True else 'this is an absurdly long line that will never be touched upon though!'
if 1 > 0:

    pass



"Final line!"
"""
    )
    return p


@pytest.fixture
def linted_test_python_file(tmp_path):
    d = tmp_path / "lint"
    d.mkdir(exist_ok=True)
    p = d / "linted.py"
    p.write_text(
        """import pandas

fake_test_string = (
    "this is an absurdly long line"
    if True
    else "this is an absurdly long line that will never be touched upon though!"
)
if 1 > 0:

    pass


"Final line!"
"""
    )
    return p
