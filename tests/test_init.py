"""
__init__.py tests
"""
import os
import pytest


def test_remove_symbols():
    """
    remove_symbols
    """
    from py23 import remove_symbols

    assert remove_symbols('c:\\win/file.txt', '/\\:.') == 'cwinfiletxt'


def test_load_module_by_path():
    """
    load_module_by_path
    """
    from py23 import load_module_by_path

    assert callable(load_module_by_path(os.path.join('py23', '__init__.py')).remove_symbols)
