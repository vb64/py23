"""
__init__.py tests
"""
import pytest


def test_remove_symbols():
    """
    remove_symbols
    """
    from py23 import remove_symbols

    assert remove_symbols('c:\\win/file.txt', '/\\:.') == 'cwinfiletxt'
