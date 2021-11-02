from datetime import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    class Meta:
        abstract = True


class Gender(models.TextChoices):
    FEMALE = 'FE', _('Женский')
    MALE = 'MA', _('Мужской')


class Tie(models.TextChoices):
    EMPTY = 'NO', _('Нет галстука')
    BLUE = 'BL', _('Голубой')
    GREEN = 'GR', _('Зеленый')
    YELLOW = 'YE', _('Желтый')


class Position(models.TextChoices):
    HELPER = 'HE', _('Помощник вожатого')
    COUNSELOR = 'CO', _('Вожатый')
    EDUCATOR = 'ED', _('Воспитатель')
    SENIOR_EDUCATOR = 'SE', _('Старший воспитатель')
    HEAD_STAFF = 'HS', _('Начальник штаба')
    HEADMASTER = 'HM', _('Начальник лагеря')
    COOK = 'CK', _('Повар')
    TOURISM_INSTRUCTOR = 'TI', _('Инструктор по туризму')
    GUARD = 'GU', _('Охранник')
    MANAGER = 'MA', _('Администратор')
    NULL = 'NU', _('null')


class Person(BaseModel):
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    patronymic = models.CharField(max_length=30, blank=True, null=True, verbose_name='Отчество')
    gender = models.CharField(
        max_length=2,
        choices=Gender.choices,
        default=Gender.FEMALE,
        verbose_name='Пол'
    )
    birthday = models.DateField(verbose_name='Дата рождения')
    parents = models.ManyToManyField('self', blank=True, related_name='children', verbose_name='Родители')
    children = models.ManyToManyField('self', blank=True, related_name='parents', verbose_name='Дети')
    siblings = models.ManyToManyField('self', blank=True, related_name='siblings', verbose_name='Братья/Сестры')
    tie = models.CharField(
        max_length=2,
        choices=Tie.choices,
        default=Tie.EMPTY,
        verbose_name='Галстук'
    )
    tie_date = models.DateField(blank=True, null=True, verbose_name='Дата получения галстука')
    is_staff = models.BooleanField(default=False, verbose_name='Сотрудник')
    staff_date = models.DateField(blank=True, null=True, verbose_name='Дата начала работы')
    position = models.CharField(
        max_length=2,
        choices=Position.choices,
        default=Position.NULL,
        verbose_name='Должность'
    )

    class Meta:
        verbose_name = 'Скаут'
        verbose_name_plural = 'Скауты'

    def __str__(self):
        if self.patronymic:
            full_name = self.surname + ' ' + self.name + ' ' + self.patronymic
        else:
            full_name = self.surname + ' ' + self.name
        return full_name

    def get_gender(self):
        return self.gender

    def get_age(self):
        birth = self.birthday
        current = datetime.now().date()
        delta = current - birth
        return delta.days // 365










