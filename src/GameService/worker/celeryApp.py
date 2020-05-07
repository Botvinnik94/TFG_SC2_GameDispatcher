from __future__ import absolute_import, unicode_literals
from celery import Celery

app = Celery('taskQueue', 
             broker='amqp://192.168.33.10',
             backend='db+postgresql://task:tiger@192.168.33.10/tasks')

if __name__ == '__main__':
    app.start()