# Student Directory

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#license)

A lightweight Django application for maintaining a student directory. It is intended for learners and small teams who need a simple browser-based interface to view student records, add new students, and manage data through Django administration.

## Key Features

- **View student records:** Display each student's name, address, and phone number in a table.
- **Add students:** Submit a CSRF-protected form to create a new student record.
- **SQLite persistence:** Store application data locally in the included SQLite database.
- **Django admin:** Manage registered student records at the admin site.
- **Template inheritance:** Share navigation and page structure through a reusable base template.

## Tech Stack

| Technology       | Purpose                           |
| ---------------- | --------------------------------- |
| Python 3.10+     | Application runtime               |
| Django 6.1       | Web framework and admin interface |
| SQLite           | Local database                    |
| Django Templates | Server-rendered HTML              |

## Getting Started

### Prerequisites

- Python 3.10 or newer
- `pip`
- A terminal opened at the repository root

### Installation

From the repository root, create and activate a virtual environment, then install the pinned dependencies:

```bash
python -m venv env
```

Windows PowerShell:

```powershell
.\env\Scripts\Activate.ps1
pip install -r requirements.txt
```

macOS/Linux:

```bash
source env/bin/activate
pip install -r requirements.txt
```

Move into this project directory before running Django commands:

```bash
cd "myProject(Django installation. Environment and project create, Model, admin, views, urls, and Read Data)"
```

### Run the application

Apply database migrations and start the development server:

```bash
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in a browser.

To create an administrator for the Django admin site:

```bash
python manage.py createsuperuser
```

Then visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Environment Variables

No environment variables are required by the current development configuration. The project uses SQLite and stores its database in `db.sqlite3`.

For production deployment, move `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` to environment variables before exposing the application publicly.

## Usage / Examples

| URL             | Action                                           |
| --------------- | ------------------------------------------------ |
| `/`             | View the student list                            |
| `/add-student/` | Open the form and add a student                  |
| `/admin/`       | Sign in and manage students through Django admin |

To add a record from the web interface:

1. Open `/add-student/`.
2. Enter the student's name, address, and phone number.
3. Select **Add Student**.
4. Confirm the new record on the student list.

## License

This project is licensed under the MIT License.
