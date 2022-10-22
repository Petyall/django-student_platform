from operator import truediv
from django.db import IntegrityError
from urllib import request
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import os
from pathlib import Path
import mimetypes
from authtest.forms import StudentRegistrationForm, UserLoginForm, WorkerRegistrationForm



 
def registration_student(request):
    if request.method == 'POST':
        user_form = StudentRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            login(request, new_user)
            return render(request, 'index.html', {'new_user': new_user})
    else:
        user_form = StudentRegistrationForm()
    return render(request, 'authtest/register.html', {'user_form': user_form})

def registration_worker(request):
    if request.method == 'POST':
        user_form = WorkerRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            login(request, new_user)
            return render(request, 'index.html', {'new_user': new_user})
    else:
        user_form = WorkerRegistrationForm()
    return render(request, 'authtest/register_worker.html', {'user_form': user_form})


def login_user(request):
    context = {'login_form': UserLoginForm()}
    if request.method == "POST":
        # Эта строка берёт всё, что написал пользователь
        # И помещает в переменную login_form для дальнейшего действия
        login_form = UserLoginForm(request.POST)
        # Если введенные данные пройдут валидацию, то выполнится условие
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            # Это условие проверки пароля (подошел или нет)
            if user:
                login(request, user)
                return redirect('index')
            else:
                context = {
                    'login_form': login_form,
                    'attention': f'Пользователь {username} или пароль не были найдены!'
                }
        # Если пользователь не зарегистрирован или пароль не подошёл,
        # то будет выполнятся это условие, которое будет брать ответ из forms.py
        # А в последствии выводится в login.html через цикл
        else:
            context = {
                'login_form': login_form,
            }
    return render(request, 'authtest/login.html', context)


def register(request):
    return render(request, 'authtest/select.html')

def logout_user(request):
    logout(request)
    return redirect('index')