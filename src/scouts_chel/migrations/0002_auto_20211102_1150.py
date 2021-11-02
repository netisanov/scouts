# Generated by Django 3.2.8 on 2021-11-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scouts_chel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Скаут', 'verbose_name_plural': 'Скауты'},
        ),
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='person',
            name='children',
            field=models.ManyToManyField(blank=True, related_name='_scouts_chel_person_children_+', to='scouts_chel.Person', verbose_name='Дети'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('FE', 'Женский'), ('MA', 'Мужской')], default='FE', max_length=2, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='person',
            name='parents',
            field=models.ManyToManyField(blank=True, related_name='_scouts_chel_person_parents_+', to='scouts_chel.Person', verbose_name='Родители'),
        ),
        migrations.AlterField(
            model_name='person',
            name='patronymic',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='person',
            name='surname',
            field=models.CharField(max_length=30, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='person',
            name='tie',
            field=models.CharField(choices=[('NO', 'Нет галстука'), ('BL', 'Голубой'), ('GR', 'Зеленый'), ('YE', 'Желтый')], default='NO', max_length=2, verbose_name='Галстук'),
        ),
        migrations.AlterField(
            model_name='person',
            name='tie_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата получения галстука'),
        ),
    ]