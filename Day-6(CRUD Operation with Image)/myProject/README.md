# Student CRUD Manager

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Pillow](https://img.shields.io/badge/Images-Pillow-306998?logo=python&logoColor=white)](https://python-pillow.org/)

## Description

Student CRUD Manager is a Django web application for maintaining student records and profile pictures. It is designed for learners and small teams that need a simple browser-based interface to create, review, update, and delete student information.

## Key Features

- **Create records:** Add a student's name, department, city, and profile picture.
- **Read records:** View all students in a Bootstrap-powered table or inspect an individual record.
- **Update records:** Edit student details and optionally replace the existing profile picture.
- **Delete records:** Remove a student record from the database.
- **Image uploads:** Store profile pictures in the configured media directory with Pillow support.
- **Admin access:** Manage `studentModel` records through Django admin.
- **SQLite persistence:** Run locally without provisioning an external database.

## Tech Stack

| Layer            | Technology                      |
| ---------------- | ------------------------------- |
| Language         | Python 3.12+                    |
| Web framework    | Django 6.1                      |
| Frontend         | Django Templates, Bootstrap 5.3 |
| Database         | SQLite                          |
| Image processing | Pillow 12.3+                    |
| Application      | `myProject`                     |
| Django app       | `myApp`                         |

## Getting Started

### Prerequisites

- Python 3.12 or newer
- Git, if cloning the repository
- A command prompt, PowerShell, or terminal

### Installation

From the project directory, create and activate a virtual environment:

```powershell
# PowerShell
cd "Day-6(CRUD Operation with Image)\myProject"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the shared project dependencies from the repository root:

```powershell
cd ..\..
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
cd "Day-6(CRUD Operation with Image)\myProject"
```

### Database Setup

Apply migrations before the first run:

```powershell
python manage.py migrate
```

To access Django admin, create a local administrator:

```powershell
python manage.py createsuperuser
```

### Run Locally

Start Django's development server:

```powershell
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for the student list. The admin interface is available at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Environment Variables

The current local configuration does not require environment variables. For any shared or deployed environment, move the hard-coded Django secret and deployment settings out of `myProject/settings.py` and provide values similar to these:

```env
DJANGO_SECRET_KEY=replace-with-a-unique-secret
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=example.com,www.example.com
```

Do not commit real secret keys or production credentials. The checked-in settings currently enable debug mode and are intended for local development only.

## Usage

1. Visit `/` to browse existing student records.
2. Select **Add Student** and submit the required student details and an optional image.
3. Use **View** to inspect a record, **Edit** to update it, or **Delete** to remove it.
4. Use `/admin/` for authenticated administrative access.

### Application Routes

| Method        | Path                   | Purpose                            |
| ------------- | ---------------------- | ---------------------------------- |
| `GET`         | `/`                    | List students                      |
| `GET`, `POST` | `/add-student/`        | Display and submit the create form |
| `GET`, `POST` | `/edit-student/<id>`   | Display and submit the edit form   |
| `GET`         | `/view-student/<id>`   | Display one student                |
| `GET`         | `/delete-student/<id>` | Delete one student                 |
| `GET`, `POST` | `/admin/`              | Django administration              |

Uploaded images are saved under the project's configured media storage. The included media serving configuration is suitable for development; use a dedicated static/media server or object storage in production.

## License

This project is intended to be released under the [MIT License](https://opensource.org/license/mit/). Add a `LICENSE` file containing the MIT License text before distributing the project.
