# Generated by Django 4.1.6 on 2023-02-17 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0006_todo_delete_todoitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='narxi',
        ),
        migrations.AddField(
            model_name='todo',
            name='narx',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='sifat',
            field=models.BooleanField(choices=[('a', 'Alo'), ('b', 'yaxshi'), ('c', 'orta')], max_length=50, null=True),
        ),
    ]
