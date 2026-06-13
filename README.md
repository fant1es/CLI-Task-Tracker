# CLI-Task-Tracker

![Git](https://img.shields.io/badge/Git-2.40-F05032?style=flat-square&logo=git&logoColor=white) ![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white) ![Click|81](https://img.shields.io/badge/CLI-Click-green?style=flat-square&logo=python&logoColor=white) ![orjson|101](https://img.shields.io/badge/JSON-orjson-green?style=flat-square&logo=json&logoColor=white)

A simple CLI to-do list tracker on Python using **click** and **orjson** libraries for creating CLI and saving data using .json file

## Tech Stack

|     Component     |                 Technology                  |
| :---------------: | :-----------------------------------------: |
|     Language      |                 Python 3.12                 |
| **CLI framework** | [Click](https://click.palletsprojects.com/) |
| **Data storage**  |    JSON file (orjson + pathlib modules)     |

## Project structure

* `cli.py` — entry point with console groups and commands description.
* `storage.py` — module for work with data storage (`storage.json`). 
* `storage.json` — data storage file (creates automatically after first start).

## Start

### 1. Cloning repository

```bash 
# Repository: https://github.com/fant1es/CLI-Task-Tracker
git clone https://github.com/fant1es/CLI-Task-Tracker.git
cd CLI-Task-Tracker
```

### 2. Installing Dependencies

```bash
python -m venv venv 

# For Linux/macOS:
source venv/bin/activate 

# For Windows:
# venv\Scripts\activate 
```

### 3. Install the package

Install the project globally inside your environment using `pyproject.toml` configurations:

```Bash
pip install .
```

If you plan to modify the source code, use `pip install -e .` to install it in editable mode.
## Usage

Once installed, the `task-tracker` tool becomes accessible directly from any directory in your terminal.

- **Check connection:**
```Bash
task-tracker hello
```

- **Add a new task:**
```Bash
task-tracker add --title "Task Title" --description "Task Description"
```

- **List all tasks** (Use optional filter `-f i` for _In progress_, `-f d` for _Done_):
```Bash
task-tracker list
task-tracker list --filter i
```

- **Update task status** (`i` for _In progress_, `d` for _Done_):
```Bash
task-tracker status [ID] [i/d]
```

- **Update task details** (You can modify title, description, or both dynamically):
```Bash
task-tracker update [ID] --title "New Title"
task-tracker update [ID] --description "New Description"
```

- **Delete a task:**
```Bash
task-tracker delete [ID]
```

## Storage

All data is saved using highly optimized JSON formatting. The file `storage.json` is safely stored globally in the user's home directory: 

* **Windows:** `C:\Users\<Username>\.config\task-tracker\storage.json` 
* **Linux/macOS:** `~/.config/task-tracker/storage.json` 

No matter from which folder you run the `task-tracker` command, you will always interact with the same task list.