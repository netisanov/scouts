# Generated by Django 3.2.8 on 2021-11-02 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scouts_chel', '0005_person_staff_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='is_staff',
            new_name='staff',
        ),
    ]
