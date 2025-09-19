from pathlib import Path
import os

# Base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad y debug
SECRET_KEY = 'django-insecure-8g6v&14!38a*ca3$r@fe7=p^$en_b#6$)_ig%$#31rfz39fy67'
DEBUG = True
ALLOWED_HOSTS = []

# Apps instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Rutas principales
ROOT_URLCONF = 'config.urls'

# Plantillas
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "posts.context_processors.sidebar_data",  # aside global
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Base de datos (SQLite por defecto)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validadores de contraseña
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Idioma y zona horaria
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_TZ = True

# Archivos estáticos (CSS/JS)
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",  # aquí vive tu carpeta assets
]
STATIC_ROOT = BASE_DIR / "staticfiles"  # usada al desplegar

# Archivos multimedia (imágenes subidas por el admin)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Campo por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
