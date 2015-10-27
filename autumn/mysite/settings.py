
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT=os.path.join(BASE_DIR, 'static') 
STATIC_URL = '/static/'
STATICFILES_DIRS = ('static')

SECRET_KEY = 'hidden'

DEBUG = False
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

if 'SERVER_SOFTWARE' in os.environ:
    from sae.const import (
        MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB
    )
else:
    # Make `python manage.py syncdb` works happy!
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = '3306'
    MYSQL_USER = 'root'
    MYSQL_PASS = ''
    MYSQL_DB   = 'autumn2sae'

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.mysql',
        'NAME':     MYSQL_DB,
        'USER':     MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST':     MYSQL_HOST,
        'PORT':     MYSQL_PORT,
    }
}


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrapform',
    'autumn',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__),'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/




FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760
DEFAULT_FILE_STORAGE = 'sae.ext.django.storage.backend.Storage'
STORAGE_BUCKET_NAME = 'media'


LOGGING = {  
    'version': 1,  
    'disable_existing_loggers': False,  
    'filters': {  
        'require_debug_false': {  
            '()': 'django.utils.log.RequireDebugFalse'  
        }  
    },  
    'handlers': {  
        'mail_admins': {  
            'level': 'ERROR',  
            'filters': ['require_debug_false'],  
            'class': 'django.utils.log.AdminEmailHandler'  
        }  
    },  
    'loggers': {  
        'django.request': {  
            'handlers': ['mail_admins'],  
            'level': 'ERROR',  
            'propagate': True,  
        },  
    }  
}