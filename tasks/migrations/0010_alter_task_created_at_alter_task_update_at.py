# Generated by Django 4.1.5 on 2023-02-06 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_alter_tasklabel_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
