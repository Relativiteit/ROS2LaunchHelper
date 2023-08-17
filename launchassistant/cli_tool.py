import click 

@click.group()
def cli():
    """ROS2 Launch File Parameter Tool"""
    pass

@click.command()
@click.argument('filepath', type=click.Path(exists=True))
def list_params(filepath):
    """List all parameters in a given launch file."""
    click.secho("Parameters for (): ...".format(filepath), fg="blue")


@click.command()
@click.argument('param_name')
@click.argument('filepath', type=click.Path(exists=True))
def validate_param(param_name, filepath):
    """Validate if a parameter exists in a the launch file"""
    #  validation for parameters
    if param_name in parase_file_for_parameters(filepath):
        click.secho("Valid parameter!", fg='green')
    else:
        click.secho("Invalid parameter!", fg="red")


cli.add_command(list_params)
cli.add_command(validate_param)


### Helper Functions ###
import xml.etree.ElementTree as ET

def parse_launch_file(filepath):
    """Parse ROS2 launch file to exxtract parameters."""
    tree = ET.parse(filepath)
    root = tree.getroot()

    # Extract parameters
    params = {}
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