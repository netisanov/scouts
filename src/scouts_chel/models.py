from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Gender(models.TextChoices):
    FEMALE = 'FE', _('Женский')
    MALE = 'MA', _('Мужской')


class Tie(models.TextChoices):
    BLUE = 'BL', _('Голубой')
    GREEN = 'GR', _('Зеленый')
    YELLOW = 'YE', _('Желтый')


class Person(BaseModel):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(
        max_length=2,
        choices=Gender.choices,
        default=Gender.FEMALE,
    )
    birthday = models.DateField()
    parents = models.ManyToManyField('self', blank=True, related_name='children')
    children = models.ManyToManyField('self', blank=True, related_name='parents')
    tie = models.CharField(
        max_length=2,
        choices=Tie.choices,
        default=Tie.BLUE,
    )
    tie_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return (timezone.now() - self.birthday).year



