from unittest.mock import MagicMock, patch

from gateways.kerlink.iStation import KerlinkIStation

BOARD_ID = "123456"


def make_device():
    return KerlinkIStation(boardid=BOARD_ID)


def test_credentials_are_derived_from_board_id():
    device = make_device()

    assert device.config["boardid"] == BOARD_ID
    assert device.config["login"] == "root"
    assert device.config["password"] == "pdmk-123456"


@patch("gateways.kerlink.iStation.SCPClient")
@patch("gateways.kerlink.iStation.paramiko.SSHClient")
def test_connect_uses_derived_host_and_credentials(mock_ssh_cls, mock_scp_cls):
    ssh = mock_ssh_cls.return_value
    device = make_device()

    result = device.connect()

    assert result is True
    ssh.connect.assert_called_once_with(
        "klk-wiis-123456.local", username="root", password="pdmk-123456"
    )
    assert device.ssh_connection is ssh
    assert device.scp_connection is mock_scp_cls.return_value


@patch("gateways.kerlink.iStation.SCPClient")
@patch("gateways.kerlink.iStation.paramiko.SSHClient")
def test_connect_returns_false_and_closes_on_failure(mock_ssh_cls, _mock_scp_cls):
    ssh = mock_ssh_cls.return_value
    ssh.connect.side_effect = OSError("unreachable")
    device = make_device()

    result = device.connect()

    assert result is False
    ssh.close.assert_called_once()
    assert device.ssh_connection is None


def test_read_network_pulls_from_expected_remote_path():
    device = make_device()
    device.scp_connection = MagicMock()

    device.readNetwork()

    device.scp_connection.get.assert_called_once_with(
        remote_path="/etc/network/connman/main.conf", local_path="."
    )


def test_write_network_pushes_to_expected_remote_path():
    device = make_device()
    device.scp_connection = MagicMock()

    device.writeNetwork("main.conf")

    device.scp_connection.put.assert_called_once_with(
        "main.conf", remote_path="/etc/network/connman/main.conf"
    )


def test_cellular_paths():
    device = make_device()
    device.scp_connection = MagicMock()

    device.readCellular()
    device.writeCellular("provisioning")

    device.scp_connection.get.assert_called_once_with(
        remote_path="/etc/network/ofono/provisioning", local_path="."
    )
    device.scp_connection.put.assert_called_once_with(
        "provisioning", remote_path="/etc/network/ofono/provisioning"
    )


def test_scp_methods_no_op_without_connection():
    device = make_device()  # never connected; scp_connection is None

    # Should not raise even though there is no connection.
    device.readNetwork()
    device.writeNetwork("main.conf")


def test_reboot_executes_remote_command():
    device = make_device()
    device.ssh_connection = MagicMock()
    device.ssh_connection.exec_command.return_value = (MagicMock(), MagicMock(), MagicMock())

    device.reboot()

    device.ssh_connection.exec_command.assert_called_once_with("reboot")
