# from django.db import models

# class Schedule(models.Model):
#     group = models.CharField(blank=True, null=True, max_length=50)
#     comment = models.FileField(upload_to='schedule/')

#     # Этот класс позволяет отображать элементы БД по времени их создания
#     class Meta:
#         verbose_name = "Расписания"
#         verbose_name_plural = "Расписания"
#         ordering = ['pk']

#     # Эта функция возвращает название в админ панели
#     def __str__(self):
#         return f'{self.group}'

#     def get_groups(self):
#         return self.group
