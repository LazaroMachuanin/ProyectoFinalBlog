from .settings import *

DEBUG = True
ALLOWED_HOSTS=['localhost', '127.0.0.1']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': ['templates'],
        #'DIRS': [os.path.join(os.path.dirname(BASE_DIR),'main','templates')],  
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR),'templates')],  
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

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR  / 'db.sqlite3',
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'main_blogdb',
        'USER': 'root',
        'PASSWORD': '1111',
        'HOST': 'localhost',
        
    }
}

#STATIC_URL = './static/'
#STATICFILES_DIRS = ('static'),
STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR),'static')),  #De donde buscar los archivos estáticos que utilizará para nuestras plantillas html (como el logo de la página, botónes o imagenes que no cambiaran por todo el recorrido de la web):


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#define el acceso a la carpeta media (la cual contendrá los archivos dinámicos que utilizarán nuestras plantillas, como puede ser una foto de perfil que suba un usuario que se registra).
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),'media')  
#MEDIA_ROOT= BASE_DIR / "media/media"

#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configuración para la clave primaria automática (si estás usando Django 3.2+)
#DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Define el acceso a la carpeta media que contendrá los archivos dinámicos
#MEDIA_URL = '/media/'
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')





#import os

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


