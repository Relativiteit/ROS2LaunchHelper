import click 
import xml.etree.ElementTree as ET
from typing import Dict

@click.group()
def cli() -> None:
    """ROS2 Launch File Parameter Tool"""
    pass

@click.command()
@click.argument('filepath', type=click.Path(exists=True))
def list_params(filepath: str) -> None:
    """List all parameters in a given launch file. """
    params = parse_launch_file(filepath)
    for name, value in params.items():
        click.secho("{}: {}".format(name, value), fg="blue")


@click.command()
@click.argument('param_name')
@click.argument('filepath', type=click.Path(exists=True))
def validate_param(param_name: str, filepath: str) -> None:
    """Validate if a parameter exists in a the launch file."""
    #  validation for parameters
    if param_name in parse_file_for_parameters(filepath):
        click.secho("Valid parameter!", fg='green')
    else:
        click.secho("Invalid parameter!", fg="red")


cli.add_command(list_params)
cli.add_command(validate_param)


### Helper Functions ###
def parse_launch_file(filepath: str) -> Dict[str, str]:
    """Parse ROS2 launch file to exxtract parameters."""
    tree = ET.parse(filepath)
    root = tree.getroot()

    # Extract parameters
    params = Dict[str, str] = {}
    for param_tag in root.findall('.//param'):
        name = param_tag.get('name')
        value = param_tag.get('value', None)
        if value is None:
            value = param_tag.text
        params[name] = value
    
    return params


# if implemented in a large project use setuptools !!
if __name__ == "__main__":
    cli()