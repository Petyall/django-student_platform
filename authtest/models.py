from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    GROUPS = (
        ('vib12', 'ВИБ12'),
        ('vib22', 'ВИБ22'),
    )

    group = models.CharField('Группа', max_length=5, choices=GROUPS, default='')

# class CustomWorker(AbstractUser):
#     TYPES = (
#         ('prepod', 'Преподаватель'),
#         ('worker', 'Сотрудник'),
#     )

#     type = models.CharField('Пол', max_length=20, choices=TYPES, default='')
