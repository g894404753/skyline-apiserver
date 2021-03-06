PYTHON ?= python3
PY_FILES := $(shell git ls-files -- *.py | xargs)

# Color
no_color = \033[0m
black = \033[0;30m
red = \033[0;31m
green = \033[0;32m
yellow = \033[0;33m
blue = \033[0;34m
purple = \033[0;35m
cyan = \033[0;36m
white = \033[0;37m


.PHONY: all
all: install fmt lint test package


.PHONY: venv
venv:
	poetry env use $(PYTHON)


.PHONY: install
install: venv
	poetry run pip install -U pip setuptools'<58.0.0'
	poetry install -vvv


.PHONY: package
package:
	poetry build


.PHONY: fmt
fmt:
	poetry run isort $(PY_FILES)
	poetry run black --config ../../pyproject.toml $(PY_FILES)
	poetry run add-trailing-comma --py36-plus --exit-zero-even-if-changed $(PY_FILES)


.PHONY: lint
lint:
	# poetry run mypy --config-file=../../mypy.ini $(PY_FILES)
	poetry run isort --check-only --diff $(PY_FILES)
	poetry run black --check --diff --color --config ../../pyproject.toml $(PY_FILES)
	poetry run flake8 $(PY_FILES)


.PHONY: test
test:
	echo TODO


.PHONY: clean
clean:
	rm -rf .venv dist


.PHONY: db_revision
HEAD_REV ?= $(shell poetry run alembic -c skyline_apiserver/db/alembic/alembic.ini heads | awk '{print $$1}')
NEW_REV ?= $(shell python3 -c 'import sys; print(f"{int(sys.argv[1])+1:03}")' $(HEAD_REV))
REV_MEG ?=
db_revision:
	$(shell [ -z "$(REV_MEG)" ] && printf '$(red)Missing required message, use "make db_revision REV_MEG=<some message>"$(no_color)')
	poetry run alembic -c skyline_apiserver/db/alembic/alembic.ini revision --autogenerate --rev-id $(NEW_REV) -m '$(REV_MEG)'


.PHONY: db_sync
db_sync:
	poetry run alembic -c skyline_apiserver/db/alembic/alembic.ini upgrade head


# Find python files without "type annotations"
future_check:
	@find src ! -size 0 -type f -name *.py -exec grep -L 'from __future__ import annotations' {} \;
