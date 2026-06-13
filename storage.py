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