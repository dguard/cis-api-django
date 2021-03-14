from __future__ import absolute_import
import asyncio
from asgiref.sync import async_to_sync, sync_to_async
import json
from celery import Celery
from celery.signals import after_setup_logger, after_setup_task_logger

import json
from django.conf import settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

import django
django.setup()

celery_app = Celery("websocket_celery")
celery_app.config_from_object('api.settings', namespace='CELERY')

# celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


import websockets
from valutes.models import Valute
from valutes.serializers import ValuteSerializer
from asgiref.sync import sync_to_async, async_to_sync
import datetime

@sync_to_async
def get_valutes():
    return list(Valute.objects.all())

async def hello():
    currentMinutes = datetime.datetime.now().strftime('%M')
    if int(currentMinutes) not in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 0]:
        print('idle %s' % datetime.datetime.now())
        return

    uri = "ws://127.0.0.1:8765"

    async with websockets.connect(uri, ping_interval=None) as websocket:
        valutes = await get_valutes()
        payload_json = json.dumps({
            'action': 'update_valutes',
            'last_updated_at': valutes[0].created_at.isoformat(),
            'results': ValuteSerializer(valutes, many=True).data
        })
        await websocket.send(payload_json)

        print(f"> {json.loads(payload_json)}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

@celery_app.task(name="send latest valutes")
def send_latest_valutes():
    async_to_sync(hello)()


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, send_latest_valutes.s(), name="send latest valutes")
