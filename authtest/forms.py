from django import forms
from django.contrib.auth.models import User
from .models import CustomUser


class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        # fields = ('username', 'first_name', 'last_name', 'email')
        fields = ('username','first_name', 'last_name', 'email', 'group')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
 
    # Это функция очистки поля, если пароль или имя пользователя неверные
    def clean(self):
        # cleaned_data берёт в себя все значения, которые ввёл пользователь
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        # Это уже сама проверка того, введено неправильное имя или пароль
        try:
            # Тут создается пользователь и если всё хорошо, то всё хорошо :)
            self.user = CustomUser.objects.get(username=username)
            # Если же пользователь не нашёлся, то выводится ошибка
        except CustomUser.DoesNotExist:
            raise forms.ValidationError(f'Пользователь {username} не существует!')
            # А если не подошел пароль, то эта
        if not self.user.check_password(password):
            raise forms.ValidationError(f'Пароль пользователя {username} введён неправильно!')

class WorkersRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        labels = {
        'username':  'Ваш никнейм',
        'first_name':  'Ваше имя',
        'last_name':  'Ваша фамилия',
        'password': 'Ваш пароль',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']