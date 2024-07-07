# Catalyst-count


Website using  the following tech stacks: Python - Django - PostgreSQL - JavaScript - Bootstrap

## How run the project?

### Clone the repository

```bash
git clone https://github.com/sagarpayghan/catalyst-count.git
cd catalyst_count
```

### Create a virtualenv and activate it

 ```bash
python3 -m venv venv
. venv/bin/activate
```

### Or on Windows cmd

 ```bash
> py -3 -m venv venv
> venv\Scripts\activate.bat
```

### Install the requirements

```bash
pip3 install -r requirements.txt
```

#### In settings.py, set up the database

for this project i used postgress, you can see the following settings below :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_user_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

#### Run makemigrations and migrate

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

#### Run the tests

```bash
python3 manage.py test
```

#### Run the development server

```bash
python3 manage.py runserver
```

Open <http://127.0.0.1:8000> in your browser.
