from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    GROUPS = (
        ('', ''),
        ('ВИБ12', 'ВИБ12'), 
        ('ВИБ22', 'ВИБ22'),
        ('ВИБ32', 'ВИБ32'),
        ('ВИБ42', 'ВИБ42'),
    )

    TYPES = (
        ('', ''),
        ('Преподаватель', 'Преподаватель'),
        ('Сотрудник', 'Сотрудник'),
    )

    group = models.CharField('Группа', max_length=5, choices=GROUPS, default=' ')
    type = models.CharField('Тип', max_length=20, choices=TYPES, default=' ')

    def __str__(self):
        return f'{self.username} - {self.group}{self.type}'

