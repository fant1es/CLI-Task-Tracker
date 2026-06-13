# Модуль для взаимодействия с JSON - файлом
import orjson
import pathlib
from dataclasses import dataclass, asdict

@dataclass
class Task:
    """Класс с данными задачи"""
    title: str
    description: str
    status: str
    id: int = None

class JSONStorage(object):
    """Класс для работы с JSON файлом"""
    def __init__(self, filename='storage.json'):
        self.file_path = pathlib.Path(filename)

        # Создание файла хранения при начале работы
        if not self.file_path.exists():
            self.file_path.touch()

            tasks_dict = {"tasks": [], "tasks_count": 0} # tasks_count для обновления id новых задач
            serialized = orjson.dumps(tasks_dict,
                                     option=orjson.OPT_INDENT_2)
            self.file_path.write_bytes(serialized)


    def add_task(self, task: Task):
        """Добавляет задачу в JSON файл"""
        try:
            all_tasks_dict = orjson.loads(self.file_path.read_bytes())

            task_dict = asdict(task)
            task_dict["id"] = all_tasks_dict["tasks_count"] + 1

            all_tasks_dict["tasks_count"] += 1
            all_tasks_dict["tasks"].append(task_dict)

            all_tasks_dict = orjson.dumps(all_tasks_dict, option=orjson.OPT_INDENT_2)
            self.file_path.write_bytes(all_tasks_dict)

        except (orjson.JSONDecodeError, orjson.JSONEncodeError, FileNotFoundError) as e:
            raise e


    def list_tasks(self, filter):
        """Отображает все хранящиеся задачи пользователю через консоль"""
        filters = {
            "i":"In progress",
            "d":"Done"
        }

        try:
            all_tasks_dict = orjson.loads(self.file_path.read_bytes())
            if filter in filters:
                filter_status = filters[filter]
                tasks = [task for task in all_tasks_dict["tasks"] if task["status"] == filters[filter]]
            else:
                tasks = all_tasks_dict["tasks"]
                filter_status = ""
            return tasks, len(tasks), filter_status

        except (orjson.JSONDecodeError, orjson.JSONEncodeError, FileNotFoundError) as e:
            raise e

    def update_task_status(self, id: int, status: str):
        """Обновляет статус задачи"""
        statuses = {
            "i":"In progress",
            "d":"Done"
        }

        try:
            all_tasks_dict = orjson.loads(self.file_path.read_bytes())
            task_index = self.find_task_index(id, all_tasks_dict["tasks"])
            all_tasks_dict["tasks"][task_index]["status"] = statuses[status]

            self.file_path.write_bytes(orjson.dumps(all_tasks_dict, option=orjson.OPT_INDENT_2))

            return all_tasks_dict["tasks"][task_index]["title"], statuses[status]

        except (orjson.JSONDecodeError, orjson.JSONEncodeError, FileNotFoundError, Exception) as e:
            raise e

    def find_task_index(self, id: int, tasks: list[dict]) -> int | None:
        """Ищет задачу и возвращает её индекс в списке all_tasks_dict["tasks"]"""
        task_index = None
        for i, task in enumerate(tasks):
            if task["id"] == id:
                task_index = i
                break

        if task_index is None:
            raise Exception(f"Task with id {id} not found")

        return task_index

    def update_task_info(self, id: int, new_title: str, new_description: str):
        """Обновляет название и описание задачи"""
        try:
            all_tasks_dict = orjson.loads(self.file_path.read_bytes())
            task_index = self.find_task_index(id, all_tasks_dict["tasks"])

            target_task = all_tasks_dict["tasks"][task_index]
            if new_title:
                target_task["title"] = new_title
            if new_description:
                target_task["description"] = new_description

            self.file_path.write_bytes(orjson.dumps(all_tasks_dict, option=orjson.OPT_INDENT_2))

            return Task(id=target_task["id"],
                        title=target_task["title"],
                        description=target_task["description"],
                        status=target_task["status"])

        except (orjson.JSONDecodeError, orjson.JSONEncodeError, FileNotFoundError, Exception) as e:
            raise e

    def delete_task(self, id: int):
        """Удаляет задание по id"""
        try:
            all_tasks_dict = orjson.loads(self.file_path.read_bytes())
            target_task_index = self.find_task_index(id, all_tasks_dict["tasks"])

            if target_task_index is not None:
                all_tasks_dict["tasks"].pop(target_task_index)
                # Нужно подумать что при удалении/добавлении с id делать
                all_tasks_dict["tasks_count"] -= 1

            self.file_path.write_bytes(orjson.dumps(all_tasks_dict, option=orjson.OPT_INDENT_2))
        except (orjson.JSONDecodeError, orjson.JSONEncodeError, FileNotFoundError, Exception) as e:
            raise e