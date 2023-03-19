import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_LOG_DIR = os.path.join(BASE_DIR, 'logs')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'normal': {
            'format': '[%(levelname)s] %(asctime)s | %(name)s | %(filename)s: %(funcName)s | %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s] %(asctime)s | %(filename)s: %(funcName)s | %(message)s'
        },
    },
    'handlers': {
        "console": {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/output.log',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 90,
            'formatter': 'normal',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'production': {
            'handler': ['console', 'file'],
            'level': 'WARNING',
            'propagate': True,
        },
        'development': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

