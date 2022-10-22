from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from authtest.forms import StudentRegistrationForm, UserLoginForm, WorkerRegistrationForm


def registration_student(request):
    if request.method == 'POST':
        user_form = StudentRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
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
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return render(request, 'index.html', {'new_user': new_user})
    else:
        user_form = WorkerRegistrationForm()
    return render(request, 'authtest/register_worker.html', {'user_form': user_form})


def login_user(request):
    context = {'login_form': UserLoginForm()}
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                context = {
                    'login_form': login_form,
                    'attention': f'Пользователь {username} или пароль не были найдены!'
                }
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
