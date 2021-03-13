from __future__ import absolute_import
from celery import Celery
from celery.signals import after_setup_logger, after_setup_task_logger

from django.conf import settings

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

import django
django.setup()

celery_app = Celery("update_valutes_celery")
celery_app.config_from_object('api.settings', namespace='CELERY')
# celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

from valutes.models import Valute

@celery_app.task
def update_valutes():
    import requests
    VALUTE_URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url = VALUTE_URL)
    data = response.json()
    Valute.objects.all().delete()

    for key, item in data['Valute'].items():
        Valute.objects.create(
            external_id=item["ID"],
            num_code=item["NumCode"],
            char_code=item["CharCode"],
            nominal=item["Nominal"],
            name=item["Name"],
            value=item["Value"],
            previous=item["Previous"]
        )


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, update_valutes.s(), name="update valutes")

