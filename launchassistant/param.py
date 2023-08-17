import click 

@click.group()
def method_collection():
    pass

""" Adding parameters to functions,
    using @click.option() and @click.argument()"""
@click.command()
@click.option("-c","--count", default=1, help='number of greetings')
@click.argument("--name")
def echo_something(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")


if __name__ == "__main__":
    method_collection()


