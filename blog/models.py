from django.db import models


class Blog(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    date = models.DateField('Дата')
    picture = models.ImageField(upload_to='static/img/', blank=True, null=True, verbose_name='Картинка')

    STATUS_SOC_LIFE = 'Социальная жизнь'
    STATUS_STUD_NEWS = 'Учебные новости'
    STATUS_UNI_LIFE = 'Жизнь ВУЗа'

    STATUS_CHOICES = [
        (STATUS_SOC_LIFE, 'Социальная жизнь'),
        (STATUS_STUD_NEWS, 'Учебные новости'),
        (STATUS_UNI_LIFE, 'Жизнь ВУЗа')
    ]
    status = models.CharField(max_length=32, choices=STATUS_CHOICES,
                              default=STATUS_SOC_LIFE, verbose_name='Состояние заказа')

    class Meta:
        verbose_name = "Статьи"
        verbose_name_plural = "Статьи"
        ordering = ['pk']

    def __str__(self):
        return self.title


