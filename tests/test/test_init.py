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


def test_win1251():
    """Check win1251 function."""
    from py23 import win1251

    assert win1251("xxx").decode('utf8') == "xxx"


def test_is_contains():
    """Check is_contains function."""
    from py23 import is_contains

    assert is_contains("xxxyyxxx", "yy")


def test_replace1251():
    """Check replace1251 function."""
    from py23 import replace1251

    assert replace1251("xyyx", "yy", "zz").decode('utf8') == "xzzx"


def test_super23():
    """Check super23 function."""
    from py23 import super23

    class ClassA(object):
        """Base class."""

        def __init__(self):
            """Make instance."""
            self.name = "class A"

    class ClassB(ClassA):
        """Child class."""

        def __init__(self):
            """Make child instance."""
            super23(self).__init__()
            self.child_name = "class B"

    assert ClassB().name == "class A"
