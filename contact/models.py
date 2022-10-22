from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя обратившегося')
    email = models.EmailField(verbose_name='Почта')
    phone_number = models.CharField(max_length=20, verbose_name='Телефон')
    theme = models.CharField(max_length=100, verbose_name='Тема вопроса')
    text = models.TextField(max_length=1000, verbose_name='Текст обращения')

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    def __str__(self):
        return f'{self.name.title()} - {self.theme.title()} - {self.phone_number}'
