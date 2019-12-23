.PHONY: all setup setup2 tests
# make tests >debug.log 2>&1

ifeq ($(OS),Windows_NT)
PYTHON = venv/Scripts/python.exe
PYTEST = venv/Scripts/pytest.exe
else
PYTHON = ./venv/bin/python
PYTEST = ./venv/bin/pytest
endif

SOURCE = py23
TESTS = tests
COVERAGE = $(PYTHON) -m coverage
PIP = $(PYTHON) -m pip install

all: tests

tests: flake8
	$(PYTEST)

flake8:
	$(PYTHON) -m flake8 --max-line-length=120 $(SOURCE)

setup2: setup_python2 setup_pip

setup: setup_python setup_pip

setup_pip:
	$(PIP) --upgrade pip
	$(PIP) -r requirements.txt
	$(PIP) -r tests/requirements.txt

setup_python:
	$(PYTHON_BIN) -m venv ./venv

setup_python2:
	$(PYTHON_BIN) -m virtualenv ./venv
