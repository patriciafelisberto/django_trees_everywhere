# Trees Everywhere Django Project

## Project Scope

The "Trees Everywhere" project aims to build a database of trees planted by volunteers around the world. Users can join an account with other users so that all can see all the trees planted by the user group of the same account. 
The project is built using the Django web framework, which is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

### Features

- User can create an account and login.
- Users associated with an account can view all the trees planted by the account's members.
- Users can add tree plantings with specific locations.
- Admin interface to manage users, accounts and tree plantings.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

Follow these steps to get your development environment running:

1. After cloning the repository, create a virtual environment to install the project's dependencies in isolation:

```shell
python3 -m venv nome-do-venv
```

2. Then activate venv with the following command:

```shell
source nome-do-venv/bin/activate
```

3. Install dependencies.

```shell
pip install -r requirements.txt
```

4. Create a `.env` file and change the environment variables

```shell
cp .env.sample .env
```

### Applying the Migrations

```python manage.py makemigrations```

```python manage.py migrate```


### Launching the Django Application

After configuring the environment, start the Flask application by running the command:
```python manage.py runserver```

### Test Execution

```python manage.py test user.tests.CustomUserModelTest```

```python manage.py test tree.tests.PlantingTestCase```