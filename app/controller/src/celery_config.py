from celery import Celery

from . import config

app = Celery("controller", broker=f"redis://{config.REDIS_HOST}:6379/0", include=["src.tasks"])

app.conf.broker_connection_retry_on_startup = True
app.autodiscover_tasks(related_name="src.tasks.send_to_manipulator")

app.conf.beat_schedule = {
    "send_to_manipulator": {
        "task": "src.tasks.send_to_manipulator",
        "schedule": config.MANIPULATOR_INTERVAL,
    },
}
