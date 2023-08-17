import click 

@click.command()
@click.option('-c','--count', default=1, help='Number of greetings.')
@click.option('-n','--name', prompt='Please enter your name', help="Enter the name of the person you want to greet.")
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times. """
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()
    
