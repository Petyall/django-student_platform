from django.db import models


class Blog(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    date = models.DateField('Дата')
    # социальная
    # жизнь, учебные
    # новости, жизнь
    # ВУЗа

    STATUS_SOC_LIFE = 'Социальная жизнь'
    STATUS_STUD_NEWS = 'Учебные новости'
    STATUS_UNI_LIFE = 'Жизнь ВУЗа'
    # Перенос этих статусов, чтобы их можно было выбирать
    STATUS_CHOICES = [
        (STATUS_SOC_LIFE, 'Социальная жизнь'),
        (STATUS_STUD_NEWS, 'Учебные новости'),
        (STATUS_UNI_LIFE, 'Жизнь ВУЗа')
    ]
    status = models.CharField(max_length=32, choices=STATUS_CHOICES,
                              default=STATUS_SOC_LIFE, verbose_name='Состояние заказа')

    def __str__(self):
        return self.title
