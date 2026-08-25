# Project1: Django CRUD Application

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description

A server-rendered Django application for managing student and teacher records through simple HTML forms. It provides a focused CRUD workflow for learners and small teams that need a lightweight local record-management example.

## Key Features

- **Student management:** Create, list, view, edit, and delete student records.
- **Teacher management:** Create, list, view, edit, and delete teacher records.
- **HTML form workflows:** Submit record changes through Django-rendered templates.
- **SQLite persistence:** Store records locally without a separate database server.
- **Django admin:** Manage both models through the built-in admin interface.
- **CSRF protection:** Use Django middleware to protect form submissions.

## Tech Stack

| Layer        | Technology                                |
| ------------ | ----------------------------------------- |
| Language     | Python 3.12+                              |
| Framework    | Django 6.1                                |
| Database     | SQLite                                    |
| Templates    | Django Templates and HTML                 |
| Dependencies | `requirements.txt` at the repository root |

## Getting Started

### Prerequisites

- Python 3.12 or newer
- Git
- A terminal with permission to create a virtual environment

### Installation

From this project directory, create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
source .venv/bin/activate
```

Install the repository dependencies. The shared dependency file is one directory above this project:

```bash
python -m pip install --upgrade pip
python -m pip install -r ../requirements.txt
```

### Run

Apply migrations and start the development server:

```bash
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in a browser.

For a new admin account, run:

```bash
python manage.py createsuperuser
```

Then visit <http://127.0.0.1:8000/admin/>.

## Environment Variables

This project does not currently require environment variables. Before deploying, move the hard-coded Django `SECRET_KEY` out of `project1/settings.py`, disable `DEBUG`, and configure `ALLOWED_HOSTS` through environment-specific settings.

## Usage

| Workflow        | URL             |
| --------------- | --------------- |
| Student list    | `/`             |
| Add student     | `/add-student/` |
| Teacher list    | `/teacher/`     |
| Add teacher     | `/add-teacher/` |
| Admin dashboard | `/admin/`       |

Use the list pages to open, edit, or delete existing records. Add forms accept a name, address, age, and phone number for each student or teacher.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
