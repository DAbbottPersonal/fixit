#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dafixup Package Installation Unit Tests
"""

from dafixup import run_requirement_generation

from .fixtures import file_with_imports


def test_requirement_file_generation(file_with_imports):
    d = file_with_imports
    run_requirement_generation(d)
    r = d / "requirements.txt"
    with open(r) as f:
        n=0
        for i, l in enumerate(f):
            n=i+1
            print(50*"-")
            print(l)
            if i == 2:
                assert "numpy" in l
            elif i == 3:
                assert "pandas" in l
        assert n == 4
