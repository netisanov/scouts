# Generated by Django 3.2.8 on 2021-11-02 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scouts_chel', '0002_auto_20211102_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='position',
            field=models.CharField(choices=[('HE', 'Помощник вожатого'), ('CO', 'Вожатый'), ('ED', 'Воспитатель'), ('SE', 'Старший воспитатель'), ('HS', 'Начальник штаба'), ('HM', 'Начальник лагеря'), ('CK', 'Повар'), ('TI', 'Инструктор по туризму'), ('GU', 'Охранник'), ('MA', 'Администратор'), ('NU', 'null')], default='NU', max_length=2, verbose_name='Должность'),
        ),
    ]