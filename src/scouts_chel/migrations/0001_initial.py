# Generated by Django 3.2.8 on 2021-11-01 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('patronymic', models.CharField(blank=True, max_length=30, null=True)),
                ('gender', models.CharField(choices=[('FE', 'Женский'), ('MA', 'Мужской')], default='FE', max_length=2)),
                ('birthday', models.DateField()),
                ('tie', models.CharField(choices=[('BL', 'Голубой'), ('GR', 'Зеленый'), ('YE', 'Желтый')], default='BL', max_length=2)),
                ('tie_date', models.DateField(default=django.utils.timezone.now)),
                ('children', models.ManyToManyField(blank=True, related_name='_scouts_chel_person_children_+', to='scouts_chel.Person')),
                ('parents', models.ManyToManyField(blank=True, related_name='_scouts_chel_person_parents_+', to='scouts_chel.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
