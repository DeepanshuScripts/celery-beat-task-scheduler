# celery_task/management/commands/create_periodic_task.py

from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule

class Command(BaseCommand):
    help = 'Create periodic tasks'

    def handle(self, *args, **kwargs):
        # Set the schedule to run every 1 minute
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.MINUTES,
        )

        # Create the periodic task
        PeriodicTask.objects.get_or_create(
            interval=schedule, 
            name='My Periodic Task',
            task='celery_task.task.my_periodic_task',
        )

        self.stdout.write(self.style.SUCCESS('Successfully created periodic task'))
