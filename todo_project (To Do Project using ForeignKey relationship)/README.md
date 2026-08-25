# To-Do Project

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#license)

A Django task-management application for authenticated users who need a simple way to create, review, update, and delete personal to-do items. It demonstrates custom user authentication, model relationships, Django forms, template inheritance, named URL navigation, and Bootstrap-based presentation.

## Contents

- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Django Template Setup](#django-template-setup)
- [Context Data](#context-data)
- [Navigation Page](#navigation-page)
- [Usage](#usage)
- [License](#license)

## Key Features

- **User registration:** Create an account with a username, full name, email, and password.
- **Authentication:** Log in, log out, and maintain a session with Django authentication.
- **Personal task list:** View only the tasks created by the signed-in user.
- **Task CRUD:** Add, edit, and delete tasks with title, description, status, and due date fields.
- **User ownership:** Associate each task with its creator through a foreign-key relationship.
- **Reusable templates:** Share navigation and page structure through a base template.
- **Responsive interface:** Use Bootstrap 5 components and layout utilities.

[Back to Contents](#contents)

## Tech Stack

| Layer              | Technology                                 |
| ------------------ | ------------------------------------------ |
| Language           | Python 3.10 or newer                       |
| Framework          | Django 6.1                                 |
| Forms              | django-crispy-forms 2.7, crispy-bootstrap5 |
| Frontend           | Django Templates, Bootstrap 5.3            |
| Database           | SQLite                                     |
| Package management | `pip`, `requirements.txt`                  |

[Back to Contents](#contents)

## Getting Started

### Prerequisites

- Python 3.10 or newer
- `pip`
- A terminal opened at the repository root

### Installation

From the repository root, create and activate a virtual environment, then install the dependencies:

```bash
cd "todo_project (To Do Project using ForeignKey relationship)"
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r ..\requirements.txt
```

On macOS or Linux:

```bash
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r ../requirements.txt
```

### Database Setup

Apply migrations before the first run:

```bash
python manage.py migrate
```

Optionally create an administrator for the Django admin site:

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in a browser. The admin site is available at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

[Back to Contents](#contents)

## Environment Variables

The current local configuration does not require environment variables. For production, move the development secret and other deployment settings out of `todo_project/settings.py`:

```env
DJANGO_SECRET_KEY=replace-with-a-long-random-value
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=example.com,www.example.com
```

Do not commit real credentials or production secrets. The included SQLite database is suitable for local development; use a managed database for production workloads.

[Back to Contents](#contents)

## Django Template Setup

Templates extend the shared base page and override its `body` block:

```html
{% extends 'master/base.html' %} {% block body %}
<h1>Welcome {{ request.user.full_name }}</h1>
{% endblock body %}
```

The shared base template includes the navigation menu and defines the common HTML document structure:

```html
{% include 'master/nav.html' %} {% block body %} {% endblock body %}
```

Templates are stored in `tasks/templates/`, and Django discovers them through `APP_DIRS=True`.

[Back to Contents](#contents)

## Context Data

The task list view filters tasks by the authenticated user and passes the result to the template with the `task_data` context key:

```python
def taskList(request):
		task_data = TaskModel.objects.filter(Created_by=request.user)
		context = {'task_data': task_data}
		return render(request, 'taskList.html', context)
```

The template reads the context data while iterating over the user's tasks:

```html
{% for task in task_data %}
<tr>
  <td>{{ task.Title }}</td>
  <td>{{ task.Status }}</td>
  <td>{{ task.Due_date }}</td>
</tr>
{% endfor %}
```

The add and edit form views also pass `form_data`, `form_heading`, and `form_btn` to the shared `master/base-form.html` template.

[Back to Contents](#contents)

## Navigation Page

The application uses named URL patterns so templates can navigate without hard-coded paths:

```python
urlpatterns = [
		path('', register_page, name='register_page'),
		path('login-page/', login_page, name='login_page'),
		path('home/', home, name='home'),
		path('task-list/', taskList, name='taskList'),
		path('add-task/', addTask, name='addTask'),
		path('edit-task/<str:p_id>', editTask, name='editTask'),
		path('delete-task/<str:p_id>', deleteTask, name='deleteTask'),
]
```

Use the `{% url %}` template tag to resolve a route by name. Pass the task ID for parameterized routes:

```html
<a href="{% url 'home' %}">Home</a>
<a href="{% url 'taskList' %}">Task List</a>
<a href="{% url 'addTask' %}">Add Task</a>
<a href="{% url 'editTask' task.id %}">Edit</a>
```

The first project-level route includes `tasks.urls`, while `/admin/` is handled by Django’s admin site.

[Back to Contents](#contents)

## Usage

1. Open `/` and register a user account.
2. Open `/login-page/` and sign in with that account.
3. Select **Task List** from the navigation menu.
4. Select **Add Task**, complete the form, and submit it.
5. Use **Edit** or **Delete** beside a task to manage it.
6. Select **Logout** when finished.

The equivalent route flow is:

```text
Register:  /
Login:     /login-page/
Home:      /home/
Tasks:     /task-list/
Create:    /add-task/
Edit:      /edit-task/<task-id>
Delete:    /delete-task/<task-id>
Logout:    /logout-page/
Admin:     /admin/
```

Task statuses are `Pending`, `Inprogress`, and `Completed`. Each task is saved with its creator through `TaskModel.Created_by`.

[Back to Contents](#contents)

## License

This project is licensed under the MIT License. Add the full MIT license text to a `LICENSE` file before distributing the project.

[Back to Contents](#contents)
