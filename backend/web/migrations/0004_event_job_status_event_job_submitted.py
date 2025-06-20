# Generated by Django 5.1.6 on 2025-02-09 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_cluster'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='job_status',
            field=models.IntegerField(choices=[(0, 'Not Submitted'), (1, 'Pending'), (2, 'Queued'), (3, 'Running'), (4, 'Completed'), (5, 'Failed'), (6, 'Cancelled')], default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='job_submitted',
            field=models.BooleanField(default=False),
        ),
    ]
