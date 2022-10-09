#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dafixup Package Installation Unit Tests
"""


def import_checker():
    try:
        import dafixup
    except ModuleNotFoundError:
        return False
    return True


def test_import():
    assert import_checker()
