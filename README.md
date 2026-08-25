# Web Application Development with Python

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

A class-wise collection of Django projects created while learning web application development with Python. The repository progresses from Django fundamentals to CRUD applications, image uploads, authentication, relationships, ModelForms, and Crispy Forms.

## Contents

- [About the Repository](#about-the-repository)
- [What I Am Learning](#what-i-am-learning)
- [Projects](#projects)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [Running a Project](#running-a-project)
- [Project Structure](#project-structure)
- [Learning Progression](#learning-progression)

## About the Repository

This repository contains practical exercises and projects from the Web Application Development with Python course. Each project is kept in its own directory with its own `manage.py` file, settings module, application code, templates, migrations, and SQLite database where applicable.

The projects are intentionally organized by class or topic so that each stage can be opened and run independently.

## What I Am Learning

- Creating Django projects and applications
- Configuring a virtual environment
- Designing models and using the Django ORM
- Running migrations and managing SQLite databases
- Registering models in Django Admin
- Connecting URLs, views, templates, and forms
- Building Create, Read, Update, and Delete workflows
- Uploading and managing images with `ImageField`
- Creating a custom user model with `AbstractUser`
- Implementing registration, login, logout, and protected pages
- Building ModelForms and validating submitted data
- Customizing form widgets
- Rendering forms with Crispy Forms and Bootstrap 5
- Creating ForeignKey relationships
- Filtering data for the authenticated user

## Projects

| Project                                                                                                                                                                                                                                                       | Main topics                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| [`myProject(Django installation. Environment and project create, Model, admin, views, urls, and Read Data)`](myProject%28Django%20installation.%20Environment%20and%20project%20create%2C%20Model%2C%20admin%2C%20views%2C%20urls%2C%20and%20Read%20Data%29/) | Django setup, models, Admin, views, URLs, templates, and reading database data |
| [`project1(CRUD Operation using HTML Form)`](project1%28CRUD%20Operation%20using%20HTML%20Form%29/)                                                                                                                                                           | CRUD operations using HTML forms and POST requests                             |
| [`Day-6(CRUD Operation with Image)`](Day-6%28CRUD%20Operation%20with%20Image%29/)                                                                                                                                                                             | CRUD operations, media files, and image uploads                                |
| [`Day-7(Django Signup operation using Abstract User)`](Day-7%28Django%20Signup%20operation%20using%20Abstract%20User%29/)                                                                                                                                     | Custom user model and user registration                                        |
| [`Day-8(Login ,Logout and Login_required method)`](Day-8%28Login%20%2CLogout%20and%20Login_required%20method%29/)                                                                                                                                             | Login, logout, authentication, and protected views                             |
| [`todo_project (To Do Project using ForeignKey relationship)`](todo_project%20%28To%20Do%20Project%20using%20ForeignKey%20relationship%29/)                                                                                                                   | Todo application, tasks, users, and ForeignKey relationships                   |
| [`Day-10(Crud Operation using Django Form)`](Day-10%28Crud%20Operation%20using%20Django%20Form%29/)                                                                                                                                                           | CRUD operations with Django ModelForms and file uploads                        |
| [`Day-11 (Crispy form and widgets)`](Day-11%20%28Crispy%20form%20and%20widgets%29/)                                                                                                                                                                           | Crispy Forms, Bootstrap 5, and custom widgets                                  |

## Technologies

| Technology                  | Purpose                                  |
| --------------------------- | ---------------------------------------- |
| Python 3.x                  | Programming language                     |
| Django 6.1                  | Web framework                            |
| SQLite                      | Local database                           |
| Bootstrap 5                 | User interface styling                   |
| Django Forms and ModelForms | Form handling and validation             |
| django-crispy-forms         | Form rendering                           |
| crispy-bootstrap5           | Bootstrap 5 integration for Crispy Forms |
| Pillow                      | Image processing and uploads             |
| Git and GitHub              | Version control and repository hosting   |

## Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd WADP_B-01-Recap-
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running a Project

Move into the directory that contains the project you want to run. For projects nested inside a class directory, move into the inner project directory first.

Example: run the todo project from the repository root:

```bash
cd "todo_project (To Do Project using ForeignKey relationship)"
python manage.py migrate
python manage.py runserver
```

Example: run the Day 11 project:

```bash
cd "Day-11 (Crispy form and widgets)/formProject"
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser. Stop the development server with `Ctrl+C`.

To create an administrator account for a project, run this from the same directory as that project's `manage.py`:

```bash
python manage.py createsuperuser
```

Then visit `http://127.0.0.1:8000/admin/`.

## Project Structure

The repository uses a class-wise layout. A typical Django project looks like this:

```text
project-directory/
├── manage.py
├── db.sqlite3
├── project_package/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── application/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── forms.py
    ├── admin.py
    ├── migrations/
    └── templates/
```

Important repository directories include:

```text
README.md
requirements.txt
env/
myProject(...)/
project1(...)/
Day-6(CRUD Operation with Image)/
Day-7(Django Signup operation using Abstract User)/
Day-8(Login ,Logout and Login_required method)/
todo_project (...)/
Day-10(Crud Operation using Django Form)/
Day-11 (Crispy form and widgets)/
```

## Learning Progression

1. **Django fundamentals:** project setup, applications, models, Admin, URLs, views, templates, and database queries.
2. **HTML form CRUD:** creating, reading, updating, and deleting records through HTML forms.
3. **Image CRUD:** handling uploaded files, media settings, and profile images.
4. **Custom users:** extending Django authentication with `AbstractUser`.
5. **Authentication:** registration, login, logout, `authenticate()`, and `login_required`.
6. **Relationships:** connecting users and tasks with `ForeignKey` and filtering user-specific data.
7. **ModelForms:** validating and simplifying database-backed form workflows.
8. **Crispy Forms:** improving form presentation with widgets and Bootstrap 5.

## Notes

- Run Django commands from the directory containing the selected project's `manage.py` file.
- The projects use SQLite for local development.
- Uploaded files are stored in project media directories where image-upload functionality is implemented.
- The included databases are development data for the course exercises.

## License

This repository is maintained for learning and educational practice.
