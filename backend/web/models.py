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


class Event(models.Model):
    """
    An event model that stores information needed to prewarm a GKE cluster.
    """

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

    def __str__(self):
        return self.name
