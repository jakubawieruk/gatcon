# GatCon

[![CI](https://github.com/jakubawieruk/gatcon/actions/workflows/ci.yml/badge.svg)](https://github.com/jakubawieruk/gatcon/actions/workflows/ci.yml)

**GatCon** is a command-line interface (CLI) application written in Python, designed to simplify the configuration of LoRaWAN gateways. It provides an interactive experience, guiding users through the process of configuring their gateways with ease.

## Supported gateways

- Kerlink Wirnet™ iStation

Support for additional gateways is added under `gateways/<vendor>/<model>.py` — see [CONTRIBUTING.md](CONTRIBUTING.md).

> **Note on credentials:** for the Kerlink iStation, GatCon uses the device's factory-default
> login (`root` / `pdmk-<board id>`). This is the gateway's own default password derived from the
> public board ID printed on the device — not a project secret.

## Installation

GatCon can be installed either by downloading pre-built files or by building the application from source.

### Prerequisites

Before installing GatCon, ensure that you have the following prerequisites:

- Python 3.13 or higher

### Installing from Release Files

To install GatCon from pre-built files:

1. Download the appropriate `.gz` or `.whl` file for your platform.
2. Open your terminal and run the following command, replacing `<version>` and `<extension>` with the appropriate values:

   ```bash
   pip install gatcon-<version>.<extension>
   ```

### Building and Installing from Source

To build and install GatCon from source:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/jakubawieruk/gatcon.git
   ```

2. Navigate to the project directory:

   ```bash
   cd gatcon
   ```

3. Install the necessary dependencies:

   ```bash
   poetry install
   ```

4. Build the application:

   ```bash
   poetry build
   ```

5. Navigate to the `dist` directory and install the package:

   ```bash
   cd dist
   pip install gatcon-<version>.<extension>
   ```

## Usage

To configure a LoRaWAN gateway you have to connect the gateway to the same network as your device.

GatCon is an interactive tool that asks about things you want to configure.

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for how to set up a
development environment, run the checks (Ruff, mypy, pytest), and add support for a new
gateway. All participants are expected to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

GatCon is released under the GNU GPL v3.0 license. For more information, see the LICENSE file.

