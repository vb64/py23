.PHONY: all setup setup2 tests
# make tests >debug.log 2>&1

ifeq ($(OS),Windows_NT)
PYTHON = venv/Scripts/python.exe
PTEST = venv/Scripts/pytest.exe
COVERAGE = venv/Scripts/coverage.exe
else
PYTHON = ./venv/bin/python
PTEST = ./venv/bin/pytest
COVERAGE = ./venv/bin/coverage
endif

SOURCE = py23
TESTS = tests
PIP = $(PYTHON) -m pip install
PYTEST = $(PTEST) --cov=$(SOURCE) --cov-report term:skip-covered
LINT = $(PYTHON) -m pylint
LINT3 = $(LINT) --init-hook="sys.path.insert(0, './')"

all: tests

tests:  flake8 lint
	$(PYTEST) --cov=$(SOURCE)
	$(COVERAGE) html --skip-covered

tests3: flake8 lint3
	$(PYTEST) --cov=$(SOURCE)
	$(COVERAGE) html --skip-covered

flake8:
	$(PYTHON) -m flake8 --max-line-length=120 $(SOURCE)

lint:
	$(LINT) $(SOURCE)

lint3:
	$(LINT3) $(SOURCE)

dist:
	$(PYTHON) setup.py sdist bdist_wheel

upload_piptest: tests dist
	$(PYTHON) -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload_pip: tests dist
	$(PYTHON) -m twine upload dist/*

setup: setup_python2 setup_pip

setup3: setup_python3 setup_pip

setup_pip:
	$(PIP) --upgrade pip
	$(PIP) -r deploy.txt
	$(PIP) -r tests/requirements.txt

setup_python3:
	$(PYTHON_BIN) -m venv ./venv

setup_python2:
	$(PYTHON_BIN) -m virtualenv ./venv
