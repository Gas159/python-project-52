# Generated by Django 4.1.5 on 2023-02-02 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0003_alter_labels_options'),
        ('tasks', '0007_alter_task_executor_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(blank=True, through='tasks.TaskLabel', to='labels.labels', verbose_name='Labels'),
        ),
    ]
