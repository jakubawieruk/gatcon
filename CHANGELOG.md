# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-07-08

### Added
- Test suite (pytest) covering config loading, ID/server validation, the Kerlink iStation
  driver, and CLI dispatch.
- GitHub Actions CI running Ruff, mypy, and pytest on Python 3.13 and 3.14.
- Dependabot configuration for weekly Python and GitHub Actions updates.

### Changed
- Minimum supported Python raised from 3.12 to 3.13; 3.14 is now supported.
- `cryptography` is no longer a direct dependency (it remains a transitive
  dependency of `paramiko`).
- Developer tooling: Ruff (lint + format), mypy, pre-commit, `.editorconfig`.
- Contributor docs: `CONTRIBUTING.md`, issue and pull request templates.
- `CLAUDE.md` and `.claude/settings.json` for AI-assisted development.
- Dependabot updates: `actions/checkout` v4→v7, `actions/setup-python` v5→v6,
  `types-paramiko` 4.x→5.x (dev).

### Fixed
- Narrowed bare `except:` blocks so `KeyboardInterrupt` / `SystemExit` are no longer swallowed.
- SCP helper methods now guard on the SCP connection they actually use.
- Corrected `confiig_path` typo in `config.load_config`.

## [0.0.2] - 2026-05

### Changed
- Updated dependencies for security (Dependabot) and bumped version.

## [0.0.1] - 2026-05

### Added
- Initial release: interactive CLI for configuring the Kerlink Wirnet™ iStation gateway
  (server, network preferences, cellular, reboot) over SSH/SCP.

[Unreleased]: https://github.com/jakubawieruk/gatcon/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/jakubawieruk/gatcon/compare/v0.0.2...v0.1.0
[0.0.2]: https://github.com/jakubawieruk/gatcon/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/jakubawieruk/gatcon/releases/tag/v0.0.1
