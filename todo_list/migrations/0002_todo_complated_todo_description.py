# Generated by Django 4.1.6 on 2023-02-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='complated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
