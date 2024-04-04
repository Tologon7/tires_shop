from pathlib import Path
from datetime import timedelta
from decouple import config
import cloudinary
# import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)


ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tires',
    'users',
    'cart',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    'drf_yasg',
    'cloudinary_storage',
    'cloudinary',
    'decouple',
    # 'drf_payments',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_TZ = True


AUTH_USER_MODEL = 'users.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
         'rest_framework_simplejwt.authentication.JWTAuthentication',
         'rest_framework.authentication.TokenAuthentication',
    ),






    # 'DEFAULT_FILTER_BACKENDS': (
    #     'django_filters.rest_framework.DjangoFilterBackend',
    # ),
}


# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.BasicAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#     ]
# }


cloudinary.config(
    cloud_name="dpcseoh6p",
    api_key="616317433996554",
    api_secret="Mitw6jRgqBD0XTIywXcURUaOz0A"
)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dpcseoh6p',
    'API_KEY': '616317433996554',
    'API_SECRET': 'Mitw6jRgqBD0XTIywXcURUaOz0A'
}


MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")


SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=7),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=2),
}


SWAGGER_SETTINGS = {
    'VALIDATOR_URL': 'http://localhost:8189',
}

#
# PAYMENT_MODEL = "stripe_checkout.StripeCheckoutPayment"
# PAYMENT_CALLBACK_URL = "http://localhost:8000/drf-payments/callback/"
# PAYMENT_SUCCESS_URL = "http://localhost:3000/payments/success/"
# PAYMENT_FAILURE_URL = "http://localhost:3000/payments/failure/"
#
# PAYMENT_VARIANTS = {
#     "stripe": (
#         "drf_payments.stripe.StripeCheckoutProvider",
#         {
#             "secret_key": os.environ.get("STRIPE_SECRET_KEY"),
#             "public_key": os.environ.get("STRIPE_PUBLIC_KEY"),
#         },
#     ),
#     "paypal": (
#         "drf_payments.paypal.PaypalProvider",
#         {
#             "client_id": os.environ.get("PAYPAL_CLIENT_ID"),
#             "secret": os.environ.get("PAYPAL_SECRET_KEY"),
#             "endpoint": os.environ.get("PAYPAL_URL", "https://api.sandbox.paypal.com"),
#         },
#     ),
# }