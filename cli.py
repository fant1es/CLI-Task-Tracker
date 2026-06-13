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
    try:
        task = Task(title=title, description=description, status="In progress")

        task.id = storage.add_task(task)

        click.echo("New task has been added:")
        click.echo(f"Task ID: {task.id}, Title: {task.title}, Status: {task.status}")
        click.echo(f"Description: {task.description}")
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


@click.command()
@click.argument("id", type=int)
@click.option("--title", "-t", help="The title of the task.", type=str, default="")
@click.option("--description", "-d", help="The description of the task.", default="", type=str)
def update(id: int, title: str, description: str):
    try:
        if not title and not description:
            click.echo(f"No title or description provided. There is nothing to update.")
            return

        updated_task = storage.update_task_info(id, title, description)

        click.echo(f"Task {id} was updated:")
        click.echo(f"Task ID: {updated_task.id}, Title: {updated_task.title}, Status: {updated_task.status}")
        click.echo(f"Description: {updated_task.description}")
    except Exception as e:
        click.echo(f"Error while updating task info: {e}")


@click.command()
@click.argument("id", type=int)
def delete(id: int):
    try:
        storage.delete_task(id)
        click.echo(f"Task {id} was deleted")
    except Exception as e:
        click.echo(f"Error while deleting task: {e}")

cli.add_command(hello)
cli.add_command(add)
cli.add_command(list)
cli.add_command(status)
cli.add_command(update)
cli.add_command(delete)

if __name__ == '__main__':
    # На время разработки определяем хранилище здесь
    storage = JSONStorage()
    cli()
