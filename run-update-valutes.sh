#/bin/bash
celery -A update_valutes_celery worker -B -l DEBUG
