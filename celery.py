from __future__ import absolute_import
from celery import Celery

app = Celery("myCeleryProject", include=["myCeleryProject.tasks"])

app.config_from_object("myCeleryProject.settings")

if __name__ == "__main__":
    app.start()
