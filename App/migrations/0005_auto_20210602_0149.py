# Generated by Django 3.1.6 on 2021-06-01 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20210602_0148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='Movie Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='movies',
            old_name='Year or Release',
            new_name='year_of_release',
        ),
    ]