import os
from pathlib import Path
from dotenv import load_dotenv

# ---------------------------
# Load Environment Variables
# ---------------------------
load_dotenv()

# ---------------------------
# Base Directory Configuration
# ---------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------
# Core Django Configuration
# ---------------------------
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS").split(",")
DEBUG = True if os.getenv("DJANGO_DEVELOPMENT_MODE").lower() == "true" else False

# ---------------------------
# Application Definition
# ---------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # -----------------------------
    # Project Applications
    # -----------------------------
    "backend",
    "crawler",
]

# ---------------------------
# Middleware Configuration
# ---------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ---------------------------
# URL Configuration
# ---------------------------
ROOT_URLCONF = "backend.urls"

# ---------------------------
# Template Configuration
# ---------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ---------------------------
# WSGI Configuration
# ---------------------------
WSGI_APPLICATION = "backend.wsgi.application"

# ---------------------------
# Database Configuration
# ---------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ---------------------------
# Password Validation
# ---------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ---------------------------
# Internationalization
# ---------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

# ---------------------------
# Static Files Configuration
# ---------------------------
STATIC_URL = "static/"

# ---------------------------
# Default Primary Key Field
# ---------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
