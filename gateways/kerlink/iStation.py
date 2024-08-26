import time
import paramiko
import click
from scp import SCPClient
from pathlib import Path
import re

TEMP_DIR = Path.home() / ".cache" / "gatcon"
class KerlinkIStation:
    def __init__(self, config:dict = None, boardid:str = None):
        self.config = {
            "manufacturer": "Kerlink",
            "model": "iStation",
            "boardid": boardid,
            "login": "root",
            "password": "pdmk-"+boardid
        }
        self.ssh_connection = None
        self.scp_connection = None

    def __del__(self):
        if self.ssh_connection:
            self.ssh_connection.close()
            click.echo("Connection closed.")

    def connect(self) -> bool:
        device = "klk-wiis-"+self.config["boardid"]+".local"
        user = self.config["login"]
        password = self.config["password"]

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(device, username=user, password=password)
            self.ssh_connection = ssh

            self.scp_connection = SCPClient(ssh.get_transport())
            return True
        except:
            click.echo("Connection failed.")
            ssh.close()
            return False

    def setServer(self, server:str) -> None:
        if not self.ssh_connection:
            click.echo("You have to connect to device first.")
            return
        ssh = self.ssh_connection
        print(f"klk_apps_config --activate-cpf --lns-server {server} --lns-dport 1700 --lns-uport 1700")
        _stdin, _stdout,_stderr = ssh.exec_command(f"klk_apps_config --activate-cpf --lns-server {server} --lns-dport 1700 --lns-uport 1700")
        
        print(_stdout.read().decode())
        time.sleep(4)
        print(_stdout.read().decode())

    def readNetwork(self) -> None:
        if not self.ssh_connection:
            click.echo("You have to connect to device first.")
            return
        self.scp_connection.get(remote_path= "/etc/network/connman/main.conf", local_path=".")
       
    def writeNetwork(self, filename) -> None:
        if not self.ssh_connection:
            click.echo("You have to connect to device first.")
            return
        self.scp_connection.put(filename, remote_path="/etc/network/connman/main.conf")

    def readCellular(self) -> None:
        if not self.ssh_connection:
            click.echo("You have to connect to device first.")
            return
        self.scp_connection.get(remote_path= "/etc/network/ofono/provisioning", local_path=".")  

    def writeCellular(self, filename) -> None:
        if not self.ssh_connection:
            click.echo("You have to connect to device first.")
            return
        self.scp_connection.put(filename, remote_path="/etc/network/ofono/provisioning")

    def reboot(self) -> None:
        if not self.ssh_connection:
            click.echo("You have to connect to device first.")
            return
        ssh = self.ssh_connection
        _stdin, _stdout,_stderr = ssh.exec_command("reboot")
        print("Device now reboot.")

    def __str__(self) -> str:
        return "Kerlink Wirnet™ iStation"

    def __repr__(self) -> str:
        return "Kerlink Wirnet™ iStation"