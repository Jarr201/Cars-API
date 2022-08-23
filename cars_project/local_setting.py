# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wzq=feja^)xa=5k9t#3f-6*x97)1ux1y6z3$yw7c=(^wcnbbw0'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "cars_database",
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}