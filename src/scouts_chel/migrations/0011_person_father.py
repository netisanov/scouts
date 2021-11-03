# Generated by Django 3.2.8 on 2021-11-03 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scouts_chel', '0010_auto_20211103_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='father',
            field=models.ForeignKey(blank=True, limit_choices_to={'gender': 'M'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children_of_father', to='scouts_chel.person'),
        ),
    ]
