import os
from pathlib import Path
import dj_database_url

# BASE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET KEY (Doit être stockée dans les variables d'environnement en production)
SECRET_KEY = os.environ.get('SECRET_KEY', 'remplacez_ceci_par_une_clé_secrète_en_production')

# DEBUG MODE (Désactivez en production)
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ALLOWED HOSTS (Ajoutez votre domaine Render ici)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

# APPLICATIONS INSTALLÉES
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',  # Pour la gestion des fichiers statiques
    'rim',  # Votre application
]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Middleware pour gérer les fichiers statiques
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL CONFIG
ROOT_URLCONF = 'cado.urls'

# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

# WSGI APPLICATION
WSGI_APPLICATION = 'cado.wsgi.application'

# BASE DE DONNÉES (Render fournit une URL de base de données via DATABASE_URL)
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}

# VALIDATION DES MOTS DE PASSE
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# LOCALISATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# FICHIERS STATIQUES
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / "rim/static"]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# FICHIERS MÉDIAS (Si vous gérez des fichiers uploadés)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# CLÉ PAR DÉFAUT POUR LES MODÈLES
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
