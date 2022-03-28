# Basic project to practice

## Structure

- `polls` - the project
- `polls/polls` - the project config
- `polls/poll` - the app that have models and views

## Commands learned

### Project schafolding

```bash
pipenv shell
```

Create an a virtual environment (venv) in the root directory.

```bash
pipenv install django
```

Install django framework in the venv

```bash
django-admin startproject project_name
```

Creates a new project in the root directory.

### Apps schafolding

```bash
python manage.py startapp app_name
```

Create an app in the project. To use that app need to refer the app config in project settings file, in that case the file will be: `polls/polls/settings.py`.

Needs to append the app config like this:

```python
# Application definition

INSTALLED_APPS = [
    'poll.apps.PollConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### Migrations

Migrate the current migrations

```bash
python manage.py migrate
```

Create a migration for specific model

```bash
python manage.py makesmigration model_name
```

### Testing

For testing our database side of application is needed to create a context to retrieve data. These context are called fixtures. Read more here: https://docs.djangoproject.com/en/4.0/howto/initial-data/

One way to create our fixtures is creating a dump or database with the command:

```bash
python manage.py dumpdata --exclude=auth --exclude=contenttypes
```

To load the fixtures to used by Django we need to run the next command:

```bash
python manage.py loaddata file.json
```
