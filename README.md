# GatCon

**GatCon** is a command-line interface (CLI) application written in Python, designed to simplify the configuration of LoRaWAN gateways. It provides an interactive experience, guiding users through the process of configuring their gateways with ease.

## Installation

GatCon can be installed either by downloading pre-built files or by building the application from source.

### Prerequisites

Before installing GatCon, ensure that you have the following prerequisites:

- Python 3.12 or higher

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

## Contribution

If you want to contribute to the development of GatCon, you can do so by following these steps:

1. Clone the repository to your device.
2. Create a new branch for your changes.
3. Make your changes.
4. Send a pull request to the main repository.

## License

GatCon is released under the GNU GPL v3.0 license. For more information, see the LICENSE file.

