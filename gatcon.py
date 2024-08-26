import click
from config import load_config
from gateways.kerlink.iStation import KerlinkIStation

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx: click.Context) -> None:
    """
    GatCon is simple tool that helps with configuration of LoRaWAN Gateways. Devices that can be configured with gatcon are listed below:
    
    - Kerlink Wirnet™ iStation
    """
    config = load_config()
    ctx.obj = {
        "config": config,
        "supported": {
            "kerlink": ["istation"]
        },
    }

    click.echo("GatCon - Gateway Configuration Tool")
    click.echo("Supported Gateways: ")
    click.echo("  - Kerlink Wirnet™ iStation")

    last6digits = click.prompt("Please enter the gateway last 6 digits of board ID")
    if not isIdValid(last6digits):
        click.echo("Invalid ID")
        return
    
    click.echo("Gatcon now will try to connect to the gateway with ID: ******" + last6digits)
    device = KerlinkIStation(boardid=last6digits)
    try:
        con = device.connect()
        click.echo("Connected to device.")

    except:
        click.echo("Connection failed.")
        return
    
    if not con:
        return
    choice = click.confirm("Do you want to configure server?")
    if choice:
        serverConfig(device)
    
    choice = click.confirm("Do you want to configure Network?")
    if choice:
        configureNetwork(device)

    choice = click.confirm("Do you want to configure cellular config?")
    if choice:
        configureCellular(device)

    # choice = click.confirm("Do you want to configure Tailscale?")
    # if choice:
    #     device.setTailScale()
    #     click.echo("Configuration completed successfully!")

    choice = click.confirm("Reboot?")
    if choice:
        device.reboot()

def isIdValid(id: str) -> bool:
    if len(id) != 6:
        return False
    return True

def validServer(server: str) -> bool:
    return True

def serverConfig(device: KerlinkIStation) -> None:
    server = click.prompt("Please enter the server address")
    if not validServer(server):
        click.echo("Invalid server address.")
        return
    device.setServer(server)
    click.echo("Server configured successfully.")

def configureNetwork(device: KerlinkIStation) -> None:
    device.readNetwork()
    with open("main.conf", "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if isinstance(line,  tuple):
            line = ''.join(line)

        if line.startswith("PreferredTechnologies ="):
            current_values = line.split('=')[1].strip().split(', ')
            break
    
    print("Current Preferred Technologies Order:")
    for index, tech in enumerate(current_values, 1):
        print(f"{index}. {tech}")
    
     # Allow the user to reorder
    print("\nEnter the new order by specifying the numbers in the desired order, separated by spaces.")
    order = input(f"New order (e.g., 1 2 3): ").strip().split()

    # Create the new ordered list
    try:
        new_order = [current_values[int(i) - 1] for i in order]
    except (IndexError, ValueError):
        print("Invalid input. Please enter numbers corresponding to the technologies.")
        return

    # Update the line in the lines list
    lines[i] = f"PreferredTechnologies = {', '.join(new_order)}\n"

    # Write the modified lines back to the file
    with open("main.conf", 'w') as file:
        file.writelines(lines)

    device.writeNetwork("main.conf")

    print("PreferredTechnologies order updated successfully.")

def configureCellular(device: KerlinkIStation) -> None:
    device.readCellular()
    with open("provisioning", 'r') as file:
        lines = file.readlines()

        # Check if the search_value exists in the file
        line_found = False
        for i, line in enumerate(lines):
            if line.strip() == "[operator:901,40]":
                print(f"Found '{"[operator:901,40]"}' at line {i+1}.")
                line_found = True
                break

        if not line_found:
            # If the line does not exist, add it and additional lines at the end
            print(f"'{"[operator:901,40]"}' not found. Adding at the end of the file.")
            additional_lines = [
                f"{"[operator:901,40]"}\n",
                "internet.AccessPointName = iot.1nce.net\n",
                "internet.Username = \n",
                "internet.Password = \n",
                "internet.AuthenticationMethod = chap\n",
                "internet.Protocol = ip\n"
            ]
            lines.extend(additional_lines)

        # Write the modified lines back to the file
        with open("provisioning", 'w') as file:
            file.writelines(lines)
        
        device.writeCellular("provisioning")

        print("File updated successfully.")