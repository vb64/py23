"""Tests __init__.py module."""
import os


def test_remove_symbols():
    """Check remove_symbols function."""
    from py23 import remove_symbols

    assert remove_symbols('c:\\win/file.txt', '/\\:.') == 'cwinfiletxt'


def test_load_module_by_path():
    """Check load_module_by_path function."""
    from py23 import load_module_by_path

    assert callable(load_module_by_path(os.path.join('py23', '__init__.py')).remove_symbols)


def test_open_text_file():
    """Check win1251 function."""
    from py23 import open_text_file

    assert open_text_file('README.md', 'r', 'utf-8')


def test_gen_next():
    """Check gen_next function."""
    from py23 import gen_next

    assert gen_next((i for i in range(2))) is not None
