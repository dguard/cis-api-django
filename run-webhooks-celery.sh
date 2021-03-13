#/bin/bash
celery -A webhooks_celery worker -B -l DEBUG
