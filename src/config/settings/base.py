"""
Django settings for ttime project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^lzsbt6o0l(l5g8&f-cu9csxli)guj*q7j$j*gnvym1#y61_q8'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'config.apps.SuitConfig',
    # 'simpleui',
    # 'adminlte3',
    # 'adminlte3_theme',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'corsheaders',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'ckeditor_uploader',
    'ckeditor',
    # Auth & social auth
    # 'dj_rest_auth',
    'allauth',
    'allauth.account',
    'dj_rest_auth.registration',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # apps
    'users',
    # 'blog',
    'product'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS_ORIGIN_WHITELIST
if os.environ.get('CORS_ALLOWED_ORIGINS'):
    CORS_ALLOWED_ORIGINS = eval(os.environ.get('CORS_ALLOWED_ORIGINS'))
else:
    CORS_ALLOWED_ORIGINS = []
# CORS_ALLOW_CREDENTIALS = True
# CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOW_METHODS = ('*')
CORS_ALLOW_HEADERS = ('*')

ROOT_URLCONF = 'config.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates'),],
#         'APP_DIRS': True,
#         'OPTIONS':
#             {
#                 'context_processors':
#                     [
#                         'django.template.context_processors.debug',
#                         'django.template.context_processors.request',
#                         'django.contrib.auth.context_processors.auth',
#                         'django.contrib.messages.context_processors.messages',
#                     ],
#             },
#     },
# ]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default':
        {
            # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'ENGINE': 'django.db.backends.postgresql',
            # Or path to database file if using sqlite3.
            'NAME': os.environ.get('DB_NAME', ''),
            # The following settings are not used with sqlite3:
            'USER': os.environ.get('DB_USER', ''),
            'PASSWORD': os.environ.get('DB_PASSWD', ''),
            # Empty for localhost through domain sockets or '127.0.0.1' for
            # localhost through TCP.
            'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
            # Set to empty string for default.
            'PORT': os.environ.get('DB_PORT', '3306'),
        }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':
        {'rest_framework.permissions.IsAdminUser'
         'rest_framework.permissions.IsAuthenticated', },
    'DEFAULT_AUTHENTICATION_CLASSES':
        (
            'dj_rest_auth.utils.JWTCookieAuthentication',
            'rest_framework_simplejwt.authentication.JWTAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.BasicAuthentication',
        ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

GOOGLE_OAUTH2_CALLBACKURL=os.environ.get('GOOGLE_OAUTH2_CALLBACKURL', '')

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (

)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/static/backend/'

DEBUG_TEMPLATE = False

_TEMPLATE_LOADERS = [
    (
        'django.template.loaders.cached.Loader',
        (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
            # 'django.template.loaders.eggs.Loader',
        )
    ),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'APP_DIRS': True,
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS':
            {
                'context_processors':
                    [
                        "django.template.context_processors.debug",
                        'django.template.context_processors.request',
                        "django.contrib.auth.context_processors.auth",
                        "django.contrib.messages.context_processors.messages",
                        # "context_processors.testing",  # Testing
                    ],
                'loaders': _TEMPLATE_LOADERS,
                'debug': DEBUG_TEMPLATE,
            }
    },
]



# List of callables that know how to import templates from various
# sources.
TEMPLATE_LOADERS = _TEMPLATE_LOADERS

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
)

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
# Disable email verification since this is just a test.
# If you want to enable it, you'll need to configure django-allauth's email confirmation pages
SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_EMAIL_REQUIRED = False

REST_USE_JWT = True

SITE_ID = 1

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True, # IMPORTANT
    'BLACKLIST_AFTER_ROTATION': True, # IMPORTANT
    'UPDATE_LAST_LOGIN': True,
}

# 配置ckeditor
CKEDITOR_UPLOAD_PATH = 'upload/'

#配置ckeditor
CKEDITOR_CONFIGS = {
    'default':
        {
            'skin':
                'moono',
            # 'skin': 'office2013',
            'toolbar_Basic': [['Source', '-', 'Bold', 'Italic']],
            'toolbar_YourCustomToolbarConfig':
                [
                    {
                        'name': 'document',
                        'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']
                    },
                    {
                        'name': 'clipboard',
                        'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']
                    },
                    {
                        'name': 'editing',
                        'items': ['Find', 'Replace', '-', 'SelectAll']
                    },
                    {
                        'name':
                            'forms',
                        'items':
                            [
                                'Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                                'HiddenField'
                            ]
                    },
                    '/',
                    {
                        'name':
                            'basicstyles',
                        'items':
                            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']
                    },
                    {
                        'name':
                            'paragraph',
                        'items':
                            [
                                'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote',
                                'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-',
                                'BidiLtr', 'BidiRtl', 'Language'
                            ]
                    },
                    {
                        'name': 'links',
                        'items': ['Link', 'Unlink', 'Anchor']
                    },
                    {
                        'name':
                            'insert',
                        'items':
                            [
                                'Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak',
                                'Iframe', 'CodeSnippet'
                            ]
                    },
                    '/',
                    {
                        'name': 'styles',
                        'items': ['Styles', 'Format', 'Font', 'FontSize']
                    },
                    {
                        'name': 'colors',
                        'items': ['TextColor', 'BGColor']
                    },
                    {
                        'name': 'tools',
                        'items': ['Maximize', 'ShowBlocks']
                    },
                    {
                        'name': 'about',
                        'items': ['About']
                    },
                    '/',  # put this to force next toolbar on new line
                    {
                        'name': 'yourcustomtools',
                        'items': [
                            # put the name of your editor.ui.addButton here
                            'Preview',
                            'Maximize',
                        ]
                    },
                    {
                        'name': 'extra',
                        'items': ['CodeSnippet', ],
                    },
                ],
            'toolbar':
                'YourCustomToolbarConfig',  # put selected toolbar config here
            # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],

            'height': 291,
            'width': '100%',
            'filebrowserWindowHeight': 725,
            'filebrowserWindowWidth': 940,
            'toolbarCanCollapse': True,
            # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
            'tabSpaces':
                4,
            'removePlugins':
                'stylesheetparser',
            'extraPlugins':
                ','.join(
                    [
                        'uploadimage',  # the upload image feature
                        # your extra plugins here
                        'div',
                        'autolink',
                        'autoembed',
                        'embedsemantic',
                        'autogrow',
                        # 'devtools',
                        'widget',
                        'lineutils',
                        'clipboard',
                        'dialog',
                        'dialogui',
                        'elementspath',
                        'codesnippet'
                    ]
                ),
        },
    # my costum tool bar i created
    'special':
        {
            'toolbar': 'Special',
            'toolbar_special': [['codeSnippet', 'Youtube'], ],
            'extraPlugins': ','.join(['codeSnippet', 'youtube']),
        }
}
# 'default': {},
# 'comment_ckeditor':
#     {
#         'toolbar': 'custom',
#         'toolbar_custom':
#             [
#                 ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
#                 ["TextColor", "BGColor", 'RemoveFormat'],
#                 ['NumberedList', 'BulletedList'],
#                 ['Link', 'Unlink'],
#                 ["Smiley", "SpecialChar", 'Blockquote', 'CodeSnippet'],
#             ],
#         'width': 'auto',
#         'height': '180',
#         'tabSpaces': 4,
#         'removePlugins': 'elementspath',
#         'resize_enabled': False,
#     }
#}

# SITENAME
ADMIN_SITE_TITLE = os.environ.get('ADMIN_SITE_TITLE', '')
ADMIN_SITE_HEADER = os.environ.get('ADMIN_SITE_HEADER', '')

# SIMPLE_UI
# SIMPLEUI_LOGIN_PARTICLES = False
SIMPLEUI_HOME_TITLE = '首頁'

# 登入相關設定login
#------------------------------------
LOGIN_URL = '/admin/login/'
LOGIN_ERROR_URL = '/admin/login/'
LOGOUT_URL = '/admin/login/'
#------------------------------------