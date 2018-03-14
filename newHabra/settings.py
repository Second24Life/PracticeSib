"""
Django settings for newHabra project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import dj_database_url
import secret_keys


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'a51y8#5vshdaim58r2o(4gkf-eiup5vwtl(42j7=cd)b+7swqn'
SECRET_KEY = os.environ.get('SECRET_KEY', secret_keys.SECRET_KEY)
GOOGLE_RECAPTCHA_SECRET_KEY = os.environ.get('GOOGLE_RECAPTCHA_SECRET_KEY',
                                             secret_keys.GOOGLE_RECAPTCHA_SECRET_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
# DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))

ALLOWED_HOSTS = ['newhabra-practicesib.herokuapp.com', ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tapeEntries',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'newHabra.urls'

LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'auth'
LOGOUT_REDIRECT_URL = 'auth'

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'newHabra.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'newhabradb',
        'USER': 'newhabrauser',
        'PASSWORD': 'betabeta',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DATABASES['default'] = dj_database_url.config(
    conn_max_age=600, ssl_require=True)


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_BROWSE_SHOW_DIRS = True

# CKEDITOR_CONFIGS = {
#         'default': {
#             'skin': 'moono',
#             # 'skin': 'office2013',
#             'toolbar_Basic': [
#                 ['Source', '-', 'Bold', 'Italic']
#             ],
#             'toolbar_YourCustomToolbarConfig': [
#                 {'name': 'document', 'items': [
#                     'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
#                 {'name': 'clipboard', 'items': [
#                     'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
#                 {'name': 'editing', 'items': [
#                     'Find', 'Replace', '-', 'SelectAll']},
#                 {'name': 'forms',
#                     'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',

#                               'HiddenField']},
#                 '/',
#                 {'name': 'basicstyles',
#                     'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
#                 {'name': 'paragraph',
#                     'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
#                               'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
#                               'Language']},
#                 {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
#                 {'name': 'insert',
#                     'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
#                 '/',
#                 {'name': 'styles', 'items': [
#                     'Styles', 'Format', 'Font', 'FontSize']},
#                 {'name': 'colors', 'items': ['TextColor', 'BGColor']},
#                 {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
#                 {'name': 'about', 'items': ['About']},
#                 '/',  # put this to force next toolbar on new line
#                 {'name': 'yourcustomtools', 'items': [
#                     # put the name of your editor.ui.addButton here
#                     'Preview',
#                     'Maximize',
#                 ]},
#             ],
#             'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
#             # 'toolbarGroups': [{ ‘name’: ‘document’, ‘groups’: [ 'mode', 'document', 'doctools' ] }],
#             # 'height': 291,
#             # 'width': '100%',
#             # 'filebrowserWindowHeight': 725,
#             # 'filebrowserWindowWidth': 940,
#             # 'toolbarCanCollapse': True,
#             # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
#             'tabSpaces': 4,
#             'removePlugins': 'stylesheetparser',
#             'extraPlugins': ','.join(
#                 [
#                     # your extra plugins here
#                     'div',
#                     'autolink',
#                     'autoembed',
#                     'embedsemantic',
#                     'autogrow',
#                     # 'devtools',
#                     'widget',
#                     'lineutils',
#                     'clipboard',
#                     'dialog',
#                     'dialogui',
#                     'elementspath',
#                     'codesnippet'
#                 ]),
#         }
#     }
