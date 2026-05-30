from unittest.mock import MagicMock, patch

from click.testing import CliRunner

import gatcon
from gatcon import cli, configureNetwork


def test_cli_rejects_invalid_board_id():
    runner = CliRunner()

    result = runner.invoke(cli, input="123\n")

    assert result.exit_code == 0
    assert "Invalid ID" in result.output


@patch("gatcon.KerlinkIStation")
def test_cli_aborts_when_connection_fails(mock_device_cls):
    mock_device_cls.return_value.connect.return_value = False
    runner = CliRunner()

    result = runner.invoke(cli, input="123456\n")

    assert result.exit_code == 0
    mock_device_cls.return_value.setServer.assert_not_called()


@patch("gatcon.KerlinkIStation")
def test_cli_dispatches_server_configuration(mock_device_cls):
    device = mock_device_cls.return_value
    device.connect.return_value = True
    runner = CliRunner()

    # board id, configure server? yes, server address, network? no, cellular? no, reboot? no
    result = runner.invoke(cli, input="123456\ny\nlns.example.com\nn\nn\nn\n")

    assert result.exit_code == 0
    device.setServer.assert_called_once_with("lns.example.com")


def test_configure_network_reorders_preferred_technologies(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    conf = tmp_path / "main.conf"
    conf.write_text("PreferredTechnologies = ethernet, wifi, cellular\n")
    monkeypatch.setattr("builtins.input", lambda _prompt: "3 2 1")
    device = MagicMock()

    configureNetwork(device)

    assert "PreferredTechnologies = cellular, wifi, ethernet" in conf.read_text()
    device.writeNetwork.assert_called_once_with("main.conf")


def test_configure_network_rejects_invalid_order(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    conf = tmp_path / "main.conf"
    conf.write_text("PreferredTechnologies = ethernet, wifi\n")
    monkeypatch.setattr("builtins.input", lambda _prompt: "9 9")
    device = MagicMock()

    configureNetwork(device)

    device.writeNetwork.assert_not_called()
    assert gatcon  # module import sanity
