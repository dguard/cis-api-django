#/bin/bash
celery -A websocket_app worker -B -l DEBUG
