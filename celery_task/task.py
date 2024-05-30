from celery import shared_task
from datetime import datetime


@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def beat_task():
    print(f"Scheduled Task Executed at {datetime.now()}")

@shared_task
def my_periodic_task():
    print(f"My periodic task executed at {datetime.now()}")