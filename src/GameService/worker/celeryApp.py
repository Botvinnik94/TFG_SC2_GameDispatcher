from __future__ import absolute_import, unicode_literals
from celery import Celery
import yaml

with open('variables.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

app = Celery('taskQueue', 
             broker=config['AMQP_URL'])

if __name__ == '__main__':
    app.start()