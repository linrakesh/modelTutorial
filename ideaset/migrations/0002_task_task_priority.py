# Generated by Django 3.1.5 on 2021-02-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideaset', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_priority',
            field=models.IntegerField(default=1),
        ),
    ]