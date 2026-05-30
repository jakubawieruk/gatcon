# CLAUDE.md

Guidance for working in the GatCon repository.

## What this is

GatCon is an interactive **CLI tool** that configures LoRaWAN gateways over SSH/SCP. It is built
with [Click](https://click.palletsprojects.com/) and managed with [Poetry](https://python-poetry.org/).
Python 3.12+ only.

## Architecture

- [`gatcon.py`](gatcon.py) — entry point. The `cli` Click group drives the interactive flow:
  prompt for a board ID → connect → optionally configure server / network / cellular → reboot.
  It also holds the small helpers (`isIdValid`, `validServer`) and the `configureNetwork` /
  `configureCellular` routines that edit config files pulled from the device.
- [`gateways/kerlink/iStation.py`](gateways/kerlink/iStation.py) — the device driver
  (`KerlinkIStation`). Encapsulates SSH (`paramiko`) and SCP (`scp`) interaction: `connect`,
  `setServer`, read/write of network and cellular config files, and `reboot`.
- [`config.py`](config.py) — load/save of the user config JSON under `~/.config/gatcon/`.

Gateway drivers follow the pattern `gateways/<vendor>/<model>.py`. To add a gateway, mirror
`KerlinkIStation` and wire it into the flow in `gatcon.py`.

## Dev commands

```bash
poetry install --with dev        # set up environment
poetry run pytest --cov          # run tests with coverage
poetry run ruff check .          # lint
poetry run ruff format .         # format
poetry run mypy .                # type check
poetry run gatcon                # run the CLI
```

## Conventions

- Prefer `click.echo` / `click.prompt` over bare `print` / `input` so output and input stay
  testable. (Some legacy `print`/`input` calls remain in the file-editing routines.)
- Catch specific exceptions, never bare `except:`.
- Type-hint new code; mypy must pass (lenient config).
- Add tests for new logic. Test pure functions directly; mock `paramiko` / `scp` for device
  interaction (see [`tests/test_istation.py`](tests/test_istation.py)).

## Gotchas

- **Credentials:** `KerlinkIStation` derives the login as `root` / `pdmk-<board id>`. This is the
  device's factory default (the board ID is printed on the unit), not a secret to be managed.
- **Working directory:** `configureNetwork` / `configureCellular` read and write `main.conf` and
  `provisioning` in the current working directory. Tests `chdir` into a tmp path to exercise them.
- The nested same-quote f-strings in `configureCellular` are valid under Python 3.12+ (PEP 701).
