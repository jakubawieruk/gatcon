# Contributing to GatCon

Thanks for your interest in improving GatCon! This guide covers how to set up your environment,
the checks we run, and how to add support for a new gateway.

By participating in this project you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Development setup

GatCon uses [Poetry](https://python-poetry.org/) and requires **Python 3.12+**.

```bash
git clone https://github.com/jakubawieruk/gatcon.git
cd gatcon
poetry install --with dev
```

(Optional) install the pre-commit hooks so lint/format run automatically on each commit:

```bash
poetry run pre-commit install
```

## Running the checks

The same checks run in CI; please make sure they pass before opening a pull request.

```bash
poetry run ruff check .          # lint
poetry run ruff format .         # auto-format (use --check to verify only)
poetry run mypy .                # type check
poetry run pytest --cov          # tests with coverage
```

## Coding conventions

- Use Click's `click.echo` / `click.prompt` for user-facing output and input (not bare
  `print` / `input`) so behavior stays testable.
- Catch specific exceptions rather than bare `except:`.
- Add type hints to new functions and methods.
- Add or update tests for any new logic. Pure functions (parsing, validation, transforms) should
  be unit-tested directly; device interaction is tested by mocking `paramiko` / `scp`.

## Adding support for a new gateway

Gateway drivers live under `gateways/<vendor>/<model>.py`. Use
[`gateways/kerlink/iStation.py`](gateways/kerlink/iStation.py) as a reference. A driver typically:

1. Derives connection details (host, credentials) from user-supplied identifiers.
2. Exposes `connect()` plus read/write methods for each configuration area.
3. Is wired into the interactive flow in [`gatcon.py`](gatcon.py).

Please include tests that mock the SSH/SCP layer and verify the remote paths and commands your
driver uses.

## Pull request flow

1. Create a branch off `main` (e.g. `feat/add-vendor-model` or `fix/short-description`).
2. Make your change with accompanying tests.
3. Ensure all checks pass locally.
4. Open a pull request describing the change and how you verified it.
5. Add an entry to [CHANGELOG.md](CHANGELOG.md) under the `Unreleased` section.
