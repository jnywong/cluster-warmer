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

    class JobStatus(models.IntegerChoices):
        """Enum for various job statuses."""

        NOT_SUBMITTED = 0
        PENDING = 1
        QUEUED = 2
        RUNNING = 3
        COMPLETED = 4
        FAILED = 5
        CANCELLED = 6

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

    # CPUs per user
    cpus_per_user = models.FloatField()

    # memory per user
    memory_per_user = models.FloatField()

    # celery job submitted?
    job_submitted = models.BooleanField(default=False)

    # celery job status
    job_status = models.IntegerField(
        default=JobStatus.NOT_SUBMITTED, choices=JobStatus.choices
    )

    def __str__(self):
        return self.name
