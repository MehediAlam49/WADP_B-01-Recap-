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
- [Pages and Tools](#pages-and-tools)
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

## Pages and Tools

Each page is connected through a named URL in `tasks/urls.py`. The snippets below show the route, view responsibility, and the main template or tool used by that page.

### 1. Registration Page

**Route:** `/` (`register_page`)

Collects account details, validates that both passwords match, creates a `CustomUserModel`, and redirects to login:

```python
path('', register_page, name='register_page')
```

The form submits the expected field names and protects the POST request with a CSRF token:

```html
<form method="POST">
  {% csrf_token %}
  <input type="text" name="full_name" />
  <input type="text" name="username" />
  <input type="email" name="email" />
  <input type="password" name="password" />
  <input type="password" name="conf_password" />
  <button type="submit">Submit</button>
</form>
```

### 2. Login Page

**Route:** `/login-page/` (`login_page`)

Authenticates the submitted username and password, starts a session with `login()`, and redirects valid users to home:

```python
path('login-page/', login_page, name='login_page')
user = authenticate(request, username=username, password=password)
if user:
		login(request, user)
		return redirect('home')
```

The page posts the credentials to its own route:

```html
<form method="POST">
  {% csrf_token %}
  <input type="text" name="username" />
  <input type="password" name="password" />
  <button type="submit">Login</button>
</form>
```

### 3. Logout Page

**Route:** `/logout-page/` (`logout_page`)

Ends the current Django session and returns the user to login:

```python
path('logout-page/', logout_page, name='logout_page')

def logout_page(request):
		logout(request)
		return redirect('login_page')
```

The shared navigation invokes it by URL name:

```html
<a href="{% url 'logout_page' %}">Logout</a>
```

### 4. Home Page

**Route:** `/home/` (`home`)

Renders the signed-in user’s basic profile information from Django’s `request.user` context object:

```python
path('home/', home, name='home')
return render(request, 'home.html')
```

```html
<h1>Welcome {{ request.user.full_name }}</h1>
<h4>Email: {{ request.user.email }}</h4>
```

### 5. Task List Page

**Route:** `/task-list/` (`taskList`)

Queries only tasks owned by the current user and sends them to `taskList.html` as `task_data`:

```python
path('task-list/', taskList, name='taskList')
task_data = TaskModel.objects.filter(Created_by=request.user)
return render(request, 'taskList.html', {'task_data': task_data})
```

```html
{% for task in task_data %}
<tr>
  <td>{{ task.Title }}</td>
  <td>{{ task.Description }}</td>
  <td>{{ task.Status }}</td>
  <td>{{ task.Due_date }}</td>
</tr>
{% endfor %}
```

### 6. Add Task Page

**Route:** `/add-task/` (`addTask`)

Displays an empty `TaskForm` on GET. On POST, it validates the form, assigns the current user, saves the task, and returns to the list:

```python
path('add-task/', addTask, name='addTask')

form_data = TaskForm(request.POST)
if form_data.is_valid():
		task = form_data.save(commit=False)
		task.Created_by = request.user
		task.save()
		return redirect('taskList')
```

The shared form template receives its page-specific labels through context:

```python
context = {
		'form_data': TaskForm(),
		'form_heading': 'Add task form',
		'form_btn': 'Add task',
}
```

### 7. Edit Task Page

**Route:** `/edit-task/<task-id>` (`editTask`)

Loads a task by ID, binds it to `TaskForm` with `instance=task_data`, and saves the edited values:

```python
path('edit-task/<str:p_id>', editTask, name='editTask')
task_data = TaskModel.objects.get(id=p_id)
form_data = TaskForm(request.POST, instance=task_data)
```

Link to the page with the task’s primary key:

```html
<a href="{% url 'editTask' task.id %}">Edit</a>
```

### 8. Delete Task Tool

**Route:** `/delete-task/<task-id>` (`deleteTask`)

Retrieves the selected task, deletes it, and redirects to the task list:

```python
path('delete-task/<str:p_id>', deleteTask, name='deleteTask')

task_data = TaskModel.objects.get(id=p_id)
task_data.delete()
return redirect('taskList')
```

```html
<a href="{% url 'deleteTask' task.id %}">Delete</a>
```

### 9. Admin Page

**Route:** `/admin/`

Create an administrator and open Django’s built-in admin interface:

```bash
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/admin/` and sign in with the superuser account.

### 10. Base Template Tool

**File:** `tasks/templates/master/base.html`

Provides the shared HTML document, Bootstrap CDN assets, navigation include, and `body` block:

```html
{% include 'master/nav.html' %} {% block body %} {% endblock body %}
```

Every page reuses it with template inheritance:

```html
{% extends 'master/base.html' %}
```

### 11. Navigation Include Tool

**File:** `tasks/templates/master/nav.html`

Centralizes links to the named routes so all pages use the same menu:

```html
<a class="nav-link" href="{% url 'home' %}">Home</a>
<a class="nav-link" href="{% url 'taskList' %}">Task List</a>
<a class="nav-link" href="{% url 'login_page' %}">Login</a>
<a class="nav-link" href="{% url 'register_page' %}">Signin</a>
<a class="nav-link" href="{% url 'logout_page' %}">Logout</a>
```

### 12. Django Forms Tool

**File:** `tasks/forms.py`

`TaskForm` is a `ModelForm` generated from `TaskModel`. The creator is excluded because the view assigns it from the authenticated session:

```python
class TaskForm(forms.ModelForm):
		class Meta:
				model = TaskModel
				fields = '__all__'
				exclude = ['Created_by']
```

The due-date field uses a browser date picker:

```python
'Due_date': forms.DateInput(
		attrs={'class': 'form-control', 'type': 'date'}
)
```

### 13. Crispy Forms Tool

Load Crispy Forms in the shared form template and render the bound form with Bootstrap 5 markup:

```html
{% load crispy_forms_tags %} {{ form_data|crispy }}
```

The required settings are:

```python
INSTALLED_APPS = [
		'crispy_forms',
		'crispy_bootstrap5',
]
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'
```

### 14. Database and Migration Tools

The project uses SQLite and Django migrations to store users and tasks:

```bash
python manage.py makemigrations tasks
python manage.py migrate
```

The task-to-user relationship is defined with a foreign key:

```python
Created_by = models.ForeignKey(
		CustomUserModel,
		on_delete=models.CASCADE,
		null=True,
)
```

### 15. Development Server Tool

Start Django’s local development server from the directory containing `manage.py`:

```bash
cd "todo_project (To Do Project using ForeignKey relationship)"
python manage.py runserver
```

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
