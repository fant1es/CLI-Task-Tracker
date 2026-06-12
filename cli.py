# Модуль со всеми консольными командами
import click
from storage import JSONStorage

@click.group()
def cli():
    pass

@click.command()
def hello():
    click.echo(f"Hello, this is simple CLI task manager!")

cli.add_command(hello)

if __name__ == '__main__':
    storage = JSONStorage()
    cli()
