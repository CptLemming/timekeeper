DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOW_ROBOTS = False

DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.mysql',
        'OPTIONS'   : {
            'init_command': 'SET storage_engine=INNODB',
        },
        'NAME'      : 'timekeeper',
        'USER'      : 'root',
        'PASSWORD'  : '',
        'HOST'      : 'localhost',
        'PORT'      : '',
    }
}