# Модуль со всеми консольными командами
import click
from storage import JSONStorage, Task

@click.group()
@click.pass_context # Для передачи ctx.obj
def cli(ctx: click.Context):
    """Главная группа команд. Инициализирует хранилище для всех подкоманд"""
    ctx.obj = JSONStorage()

@click.command()
def hello():
    click.echo(f"Hello, this is simple CLI task manager!")


@click.command()
@click.option("--title", "-t", help="The title of the task.",
              prompt="Enter the title of the task", type=str)
@click.option("--description", "-d", help="The description of the task.",
              prompt="Enter the description of the task", type=str)
@click.pass_context
def add(ctx: click.Context, title: str, description: str):
    try:
        task = Task(title=title, description=description, status="In progress")

        task.id = ctx.obj.add_task(task)

        click.echo("New task has been added:")
        click.echo(f"Task ID: {task.id}, Title: {task.title}, Status: {task.status}")
        click.echo(f"Description: {task.description}")
    except Exception as e:
        click.echo(f"Error while adding task: {e}")


@click.command()
@click.option("--filter", "-f", help="The filter of the task.", type=str, default="all")
@click.pass_context
def list(ctx: click.Context, filter: str):
    try:
        tasks, tasks_count, filter_status = ctx.obj.list_tasks(filter)

        click.echo(f"Total tasks {filter_status.lower()}: {tasks_count}")
        for task in tasks:
            click.echo(f"\nTask ID: {task['id']}, Title: {task['title']}, Status: {task['status']}")
            click.echo(f"Description: {task['description']}")

    except Exception as e:
        click.echo(f"Error while listing tasks: {e}")


@click.command()
@click.argument("id", type=int)
@click.argument("status", type=str)
@click.pass_context
def status(ctx: click.Context, id: int, status: str):
    try:
        if status not in ["i", "d"]:
            click.echo(f"Invalid status value: {status}, must be 'i' or 'd'")
            return

        task_title, new_status = ctx.obj.update_task_status(id, status)
        click.echo(f"Task {task_title} was updated to '{new_status}'")
    except Exception as e:
        click.echo(f"Error while updating task status: {e}")


@click.command()
@click.argument("id", type=int)
@click.option("--title", "-t", help="The title of the task.", type=str, default="")
@click.option("--description", "-d", help="The description of the task.", default="", type=str)
@click.pass_context
def update(ctx: click.Context, id: int, title: str, description: str):
    try:
        if not title and not description:
            click.echo(f"No title or description provided. There is nothing to update.")
            return

        updated_task = ctx.obj.update_task_info(id, title, description)

        click.echo(f"Task {id} was updated:")
        click.echo(f"Task ID: {updated_task.id}, Title: {updated_task.title}, Status: {updated_task.status}")
        click.echo(f"Description: {updated_task.description}")
    except Exception as e:
        click.echo(f"Error while updating task info: {e}")


@click.command()
@click.argument("id", type=int)
@click.pass_context
def delete(ctx: click.Context, id: int):
    try:
        ctx.obj.delete_task(id)
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
    cli()
