from __future__ import absolute_import
from celery import Celery
from celery.signals import after_setup_logger, after_setup_task_logger
import json
from django.conf import settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

import django
django.setup()

celery_app = Celery("webhooks_celery")
celery_app.config_from_object('api.settings', namespace='CELERY')
# celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

from valutes.models import Valute
from webhooks.models import Webhook
from valutes.serializers import ValuteSerializer
import datetime

@celery_app.task
def send_webhook():
    currentMinutes = datetime.datetime.now().strftime('%M')
    if int(currentMinutes) not in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 0]:
        print('idle %s' % datetime.datetime.now())
        return

    import requests
    payload_json = ValuteSerializer(Valute.objects.all(), many=True).data

    webhooks = Webhook.objects.all()
    for webhook in webhooks:
        callback_url = webhook.callback_url
        print("send post request to %s" % callback_url)

        response = requests.post(url=callback_url, json=payload_json)
        try:
            data = response.json()
            print("received response from %s" % callback_url)
        except:
            print("no response from %s" % callback_url)


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, send_webhook.s(), name="send webhook")
