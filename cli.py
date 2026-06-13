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


@click.command()
@click.option("--filter", "-f", help="The filter of the task.", type=str, default="all")
def list(filter: str):
    try:
        tasks, tasks_count, filter_status = storage.list_tasks(filter)

        click.echo(f"Total tasks {filter_status.lower()}: {tasks_count}")
        for task in tasks:
            click.echo(f"\nTask ID: {task['id']}, Title: {task['title']}, Status: {task['status']}")
            click.echo(f"Description: {task['description']}")

    except Exception as e:
        click.echo(f"Error while listing tasks: {e}")


@click.command()
@click.argument("id", type=int)
@click.argument("status", type=str)
def status(id: int, status: str):
    try:
        if status not in ["i", "d"]:
            click.echo(f"Invalid status value: {status}, must be 'i' or 'd'")
            return

        task_title, new_status = storage.update_task_status(id, status)
        click.echo(f"Task {task_title} was updated to '{new_status}'")
    except Exception as e:
        click.echo(f"Error while updating task status: {e}")

cli.add_command(hello)
cli.add_command(add)
cli.add_command(list)
cli.add_command(status)

if __name__ == '__main__':
    # На время разработки определяем хранилище здесь
    storage = JSONStorage()
    cli()
