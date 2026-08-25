# Django Product CRUD Form

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.8-7952B3?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![SQLite](https://img.shields.io/badge/SQLite-database-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](#license)

## Contents

- [Description](#description)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Django Template Setup](#django-template-setup)
- [Context Data](#context-data)
- [Navigation Page](#navigation-page)
- [Usage](#usage)
- [License](#license)

## Description

A focused Django learning project for managing a product catalog with server-rendered forms. It demonstrates how developers can build create, read, update, and delete workflows with Django `ModelForm`, SQLite, image uploads, reusable templates, and named URL navigation.

## Key Features

- **Product catalog:** Displays product name, price, description, quantity, and image.
- **Create products:** Saves validated form submissions and uploaded images.
- **Update products:** Loads an existing product into the same reusable form template.
- **Delete products:** Removes a product and returns to the catalog.
- **Reusable templates:** Shares layout and navigation through template inheritance and includes.
- **Named URLs:** Uses Django URL names for maintainable links between pages.
- **Responsive UI:** Uses Bootstrap 5.3.8 for the form and product table presentation.

## Tech Stack

| Technology      | Purpose                                |
| --------------- | -------------------------------------- |
| Python 3.12+    | Application runtime                    |
| Django 6.1      | Web framework, routing, forms, and ORM |
| SQLite          | Local development database             |
| Pillow          | ImageField support                     |
| Bootstrap 5.3.8 | Responsive presentation layer via CDN  |

## Getting Started

### Prerequisites

- Python 3.12 or newer
- `pip`
- A terminal opened at the repository root

### Installation

```bash
git clone <repository-url>
cd WADP_B-01-Recap-
python -m venv env
```

Activate the virtual environment:

```bash
# Windows PowerShell
.\env\Scripts\Activate.ps1

# Windows Command Prompt
env\Scripts\activate.bat
```

Install the project dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Run the application

Run the remaining commands from the Django project directory:

```bash
cd "Day-10(Crud Operation using Django Form)\formProject"
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in a browser. The bundled SQLite database and initial migration are included for local learning and demonstration.

## Environment Variables

This learning project does not currently require environment variables. For a production deployment, move the secret key and deployment settings out of `formProject/settings.py`:

```env
DJANGO_SECRET_KEY=replace-with-a-long-random-value
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=example.com,www.example.com
```

The settings module must be updated to read these values before using them in a deployed environment.

## Django Template Setup

The shared base template defines the document shell, loads Bootstrap, includes the navigation partial, and exposes a content block:

```html
<!-- formApp/templates/master/base.html -->
{% include 'master/nav.html' %} {% block content %} {% endblock content %}
```

Pages inherit that layout instead of duplicating the HTML shell:

```html
<!-- formApp/templates/productList.html -->
{% extends 'master/base.html' %} {% block content %}
<h2>Product List</h2>
<a href="{% url 'addProduct' %}">Add Product</a>
{% endblock %}
```

The shared form supports both create and update operations. File uploads require `multipart/form-data` and CSRF protection:

```html
<form method="POST" enctype="multipart/form-data">
  {% csrf_token %} {{ form_data }}
  <button type="submit">{{ form_btn }}</button>
</form>
```

## Context Data

Views pass dictionaries to templates with `render`. The list page exposes all products:

```python
def productList(request):
		products = productModel.objects.all()
		context = {'products': products}
		return render(request, 'productList.html', context)
```

The reusable form template receives the form instance and display values from both add and edit views:

```python
context = {
		'form_data': form_data,
		'form_heading': 'Add Product Form',
		'form_btn': 'Add Product',
}
return render(request, 'master/base-form.html', context)
```

## Navigation Page

The root URL configuration includes the app URLs, so the following named routes are available from the site root:

```python
# formApp/urls.py
urlpatterns = [
		path('', productList, name='productList'),
		path('add-product/', addProduct, name='addProduct'),
		path('edit-product/<str:p_id>', editProduct, name='editProduct'),
		path('delete-product/<str:p_id>', deleteProduct, name='deleteProduct'),
]
```

Use URL names in templates rather than hard-coded paths. Detail pages receive the product ID as `p_id`:

```html
<a href="{% url 'productList' %}">Product List</a>
<a href="{% url 'addProduct' %}">Add Product</a>
<a href="{% url 'editProduct' product.id %}">Edit</a>
<a href="{% url 'deleteProduct' product.id %}">Delete</a>
```

## Usage

1. Visit `/` to review the product list.
2. Select **Add Product**, complete the fields, optionally upload an image, and submit the form.
3. Select **Edit** beside a product to update its values.
4. Select **Delete** to remove a product and return to `/`.

The equivalent browser paths are:

```text
GET  /                         # List products
GET  /add-product/             # Show the create form
POST /add-product/             # Create a product
GET  /edit-product/<id>        # Show the update form
POST /edit-product/<id>        # Update a product
GET  /delete-product/<id>      # Delete a product
```

## License

This project is released under the MIT License. Add a `LICENSE` file containing the standard MIT License text before distributing the repository.
