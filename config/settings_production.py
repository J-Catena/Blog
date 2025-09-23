from .settings import *  # importa todo lo común

# 🔹 Cambios para producción
DEBUG = False

ALLOWED_HOSTS = ["jcatena.pythonanywhere.com"]

CSRF_TRUSTED_ORIGINS = ["https://jcatena.pythonanywhere.com"]
