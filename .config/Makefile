PACKAGE_NAME := security-scanner
OWNER := TheNewThinkTank

.PHONY: extract-version check-pypi-version setup-python install-deps build-package

# Install and cache poetry
.PHONY: install-poetry
install-poetry:
	curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies with poetry
.PHONY: install-dependencies
install-dependencies:
	poetry install
	env POETRY_VIRTUALENVS_IN_PROJECT=true

# Lint with flake8
.PHONY: lint-flake8
lint-flake8:
	poetry run flake8 --ignore=E123,E126,E203,E402,E501,F401 --exclude=.venv .

# Lint with ruff
.PHONY: lint-ruff
lint-ruff:
	poetry run ruff check

# Static type checks with mypy
.PHONY: static-type-checks
static-type-checks:
	poetry run mypy profiling_tools/ --exclude '/site-packages/'

# Extract tag details from GitHub Actions environment variables
extract-version:
	@TAG_NAME=$$(echo $${GITHUB_REF#refs/tags/}) && \
	NEW_VERSION=$$(echo $$TAG_NAME | awk -F'-' '{print $$1}') && \
	SUFFIX=$$(echo $$TAG_NAME | grep -oP '[a-z]+[0-9]+' || echo "") && \
	echo "new_version=$$NEW_VERSION" >> $GITHUB_OUTPUT && \
	echo "suffix=$$SUFFIX" >> $GITHUB_OUTPUT && \
	echo "tag_name=$$TAG_NAME" >> $GITHUB_OUTPUT

# Check if the new version is greater than the latest on PyPI
check-pypi-version:
	@response=$$(curl -s https://pypi.org/pypi/${PACKAGE_NAME}/json || echo "{}") && \
	latest_previous_version=$$(echo $$response | grep -oP '"releases":\{"\K[^"]+' | sort -rV | head -n 1) && \
	if [ -z "$$latest_previous_version" ]; then \
		latest_previous_version="0.0.0"; \
	fi && \
	echo "latest_previous_version=$$latest_previous_version" >> $GITHUB_ENV

# Set up Python and Poetry
setup-python:
	curl -sSL https://install.python-poetry.org | python3 -
	echo "$$HOME/.local/bin" >> $$GITHUB_PATH
	poetry install --sync --no-interaction

# Build source and wheel distribution
build-package:
	poetry build
