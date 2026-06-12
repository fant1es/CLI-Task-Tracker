# Модуль со всеми консольными командами
import click
from storage import JSONStorage, Task

@click.group()
def cli():
    pass

@click.command()
def hello():
    click.echo(f"Hello, this is simple CLI task manager!")


@click.command()
@click.option("--title", "-t", help="The title of the task.",
              prompt="Enter the title of the task", type=str)
@click.option("--description", "-d", help="The description of the task.",
              prompt="Enter the description of the task", type=str)
def add(title: str, description: str):
    click.echo(f"Adding {title} to {description}")
    task = Task(title=title, description=description, status="In progress")

    try:
        storage.add_task(task)
    except Exception as e:
        click.echo(f"Error while adding task: {e}")

cli.add_command(hello)
cli.add_command(add)

if __name__ == '__main__':
    # На время разработки определяем хранилище здесь
    storage = JSONStorage()
    cli()
