# Generated by Django 4.1.2 on 2022-10-22 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authtest', '0002_customuser_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='type',
            field=models.CharField(choices=[('prepod', 'Преподаватель'), ('worker', 'Сотрудник')], default='', max_length=20, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='group',
            field=models.CharField(choices=[('vib12', 'ВИБ12'), ('vib22', 'ВИБ22')], default='', max_length=5, verbose_name='Группа'),
        ),
    ]
