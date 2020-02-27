
__version__ = "11.4.10"

# https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery_setup import celery_app

# TODO: Unless its actually required, consider removing this entry
__all__ = ('celery_app',)


