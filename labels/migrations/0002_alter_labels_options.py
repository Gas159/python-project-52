# Generated by Django 4.1.5 on 2023-01-29 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='labels',
            options={'verbose_name': '=Label=', 'verbose_name_plural': '=Labels='},
        ),
    ]
