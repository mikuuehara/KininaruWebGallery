import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '^_@rll+8ebui7exl^m+4ke1ws^tvi-6nyje6v%j6rw$q%$rruo'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True