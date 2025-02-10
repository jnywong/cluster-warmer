from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    A custom user model is highly recommended by Django, as migrating to one later
    in the project is challenging. For more information see:
    https://docs.djangoproject.com/en/5.2/topics/auth/customizing/
    """

    # make sure email is unique for each user
    email = models.EmailField(unique=True)


class Cluster(models.Model):
    """
    Store cluster information retrieved from GKE API.

    See management > commands > read_clusters.py
    """

    name = models.CharField(max_length=128)
    machine_type = models.CharField(max_length=128)
    cpus = models.IntegerField()
    memory = models.IntegerField()  # GB


class Event(models.Model):
    """
    An event model that stores information needed to prewarm a GKE cluster.
    """

    class TaskStatus(models.IntegerChoices):
        """Enum for various celery task statuses."""

        NOT_SUBMITTED = 0
        PENDING = 1
        RUNNING = 2
        COMPLETED = 3
        FAILED = 4
        CANCELLED = 5

    def get_machines():
        return {i: i for i in settings.MACHINE_LIST}

    # id
    id = models.AutoField(primary_key=True)  # noqa

    # the name of the event
    name = models.CharField(max_length=128)

    # the event's description
    description = models.TextField(blank=True)

    # the event's start time
    start_time = models.DateTimeField()

    # the event's end time
    end_time = models.DateTimeField()

    # number of users
    num_users = models.IntegerField()

    # machine type
    machine = models.TextField(choices=get_machines())

    # celery task submitted?
    task_submitted = models.BooleanField(default=False)

    # celery task status
    task_status = models.IntegerField(
        default=TaskStatus.NOT_SUBMITTED, choices=TaskStatus.choices
    )

    # celery task_id
    task_id = models.CharField(max_length=128, blank=True)
