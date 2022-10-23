# Команда HelloWorld, кейс от компании «Вебпрактик» - площадка для студентов и сотрудников ВУЗа.

Мы реализовали аутентификацию пользователей (как для студента, так и для сотрудника), просмотр и загрузка расписания из личного кабинета, обратная связь с ректором и статьи с различными категориями.

Увидеть сайт можно по этой
[ссылке](https://petyal.ru).

## Установка

1:

    git clone https://github.com/Petyall/hackaton2022.git 

2:

    cd hackaton2022

3:

    python -m venv venv
    
4:

    venv\Scripts\activate
 
5:

    pip install -r requirements.txt

6:

    python manage.py runserver
7:

    Логин и пароль для админ панели (127.0.0.1:8000/admin/):
    Логин - petyal
    Пароль - 1


# Если будет такая ошибка при установке зависимостей:
ERROR: Failed building wheel for backports.zoneinfo
ERROR: Could not build wheels for backports.zoneinfo, which is required to install pyproject.toml-based projects

1:
    Пишем в requirements.txt данный текст:
    backports.zoneinfo==0.2.1; python_version<"3.9"