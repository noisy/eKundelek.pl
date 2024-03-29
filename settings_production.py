from ekundelek.settings import *

DEBUG = False

ADMINS = (
    ('Krzysztof Szumny', 'kszumny@spistresci.pl'),
    ('Magdalena Szumna', 'mszumna@spistresci.pl'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django_ekundelek',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    },
}

EMAIL_SUBJECT_PREFIX= 'Nowy eKundelek: '
