from .settings import *

DEBUG = True

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
        'NAME': 'blogwebdb',
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