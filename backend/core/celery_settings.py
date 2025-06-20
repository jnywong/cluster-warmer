"""
Settings for Celery to run tasks.
"""

from celery.schedules import crontab

CELERY_TIMEZONE = "UTC"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_RESULT_BACKEND = "django-db"
CELERY_RESULT_EXTENDED = True
CELERY_CACHE_BACKEND = "default"

CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
CELERY_TASK_RESULT_EXPIRES = 6000

CELERY_BROKER_URL = "amqp://"

# Don't use pickle as serializer, json is much safer
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["pickle", "application/json"]

CELERYD_HIJACK_ROOT_LOGGER = False
CELERYD_PREFETCH_MULTIPLIER = 1
CELERYD_MAX_TASKS_PER_CHILD = 1000

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
celery_queue = "celery"
CELERY_BEAT_SCHEDULE = {
    "task-nodepool-size": {
        "task": "web.tasks.nodepool_size",
        "schedule": crontab(minute="*"),
        "options": {"queue": celery_queue},
    },
}
