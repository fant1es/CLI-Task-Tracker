# Модуль для взаимодействия с JSON - файлом
import pathlib

class JSONStorage(object):
    def __init__(self, filename='storage.json'):
        file_path = pathlib.Path(filename)
        # Создание файла хранения при начале работы
        if not file_path.exists():
            pathlib.Path('storage.json').touch()
