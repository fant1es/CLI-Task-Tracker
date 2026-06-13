# CLI-Task-Tracker

![Git](https://img.shields.io/badge/Git-2.40-F05032?style=flat-square&logo=git&logoColor=white) ![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white) ![Click](https://img.shields.io/badge/CLI-Click-green?style=flat-square&logo=python&logoColor=white)

A simple CLI to-do list tracker on Python using **click** library for creating CLI and saving data using .json file

## Tech Stack

|     Language      |                 Python 3.12                 |
| :---------------: | :-----------------------------------------: |
| **CLI framework** | [Click](https://click.palletsprojects.com/) |
| **Data storage** |     JSON file (json + pathlib modules)      |

## Project structure
* `cli.py` — entry point with console groups and commands description.
* `storage.py` — module for work with data storage (`storage.json`). 
* `storage.json` — data storage file (creates automatically after first start).

## Fast start

### 1. Cloning repository
```bash 
# Repository: [https://github.com/fant1es/CLI-Task-Tracker](https://github.com/fant1es/CLI-Task-Tracker)
git clone [https://github.com/fant1es/CLI-Task-Tracker.git](https://github.com/fant1es/CLI-Task-Tracker.git)
cd CLI-Task-Tracker
```

### 2. Installing Dependencies
```bash
python -m venv venv 

# For Linux/macOS:
source venv/bin/activate 

# For Windows:
# venv\Scripts\activate 

pip install click
```

### 3. Start
Checking base command:
```bash
python cli.py hello
```
Console output: `Hello, this is simple CLI task manager!`

## Roadmap
- [x] `add [title] [description]` — add new task.
- [x] `list` — print all tasks (with possible status filters).
- [ ] `update [id] [new title] [new description]` — edit task info.
- [ ] `delete [id]` — delete task by id.
- [ ] `status [id] [status]` — change task status.