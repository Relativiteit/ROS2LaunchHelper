import click 

@click.group()
def cli():
    pass

@click.command()
def hello():
    click.secho('hello world', fg='red')
    click.secho('Good morning', fg='black', bg='yellow')
    click.secho('Warning', blink=True, bold=True)

@click.command()
def initdb():
    click.secho('Initialized the database', fg="white", bg="green" )

@click.command()
def dropdb():
    click.secho("Dropped the database", bg="yellow")


cli.add_command(initdb)
cli.add_command(dropdb)
cli.add_command(hello)


if __name__ == '__main__':
    cli()
