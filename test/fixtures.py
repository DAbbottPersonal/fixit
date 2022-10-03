#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fixtures for Unit Tests
"""
import pytest


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
    print(p)
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
