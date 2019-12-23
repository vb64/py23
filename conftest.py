"""
pytest session setup
"""
import sys
import os
import pytest


@pytest.fixture(scope="session", autouse=True)
def session_setup(request):
    """ 
    Auto session resource fixture
    """
    src = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(1, src)
