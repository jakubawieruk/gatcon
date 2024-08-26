# GatCon

GatCon is a CLI (Command Line Interface) application written in Python that helps with LoRaWAN Gateway configuration.


The project uses Poetry tool for dependency management.

## Installation

To install GatCon you can download already built files or make a build yourself

### Prerequisites

1. Python >3.12

### From relase files

1. Download .gz or .whl file
2. Run in terminal `pip install gatcon-<version>.<extension>`

### Build and install

1. Clone the repository to your device.
2. Navigate to the project directory.
3. Run the `poetry install` command to install all dependencies.
4. Run the `poetry build` command to make a build.
5. Go to `/dist` and install with your package manager

## Usage

To configure a LoRaWAN gateway you have to connect the gateway to the same network as your device.

GatCon is an interactive tool that asks about things you want to configure.

## Contribution

If you want to contribute to the development of GatCon, you can do so by following these steps:

1. Clone the repository to your device.
2. Create a new branch for your changes.
3. Make your changes.
4. Send a pull request to the main repository.

## License

GatCon is released under the GNU GPL v3.0 license. For more information, see the LICENSE file.

