from contact.models import Contact
from django.forms import ModelForm, TextInput, Textarea


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone_number", "theme", "text"]
        widgets = {
            "name": TextInput(attrs={
                'placeholder': 'Ваше имя'
            }),
            "email": TextInput(attrs={
                'placeholder': 'Ваша почта'
            }),
            "phone_number": TextInput(attrs={
                'placeholder': 'Ваш номер телефона'
            }),
            "theme": TextInput(attrs={
                'placeholder': 'Тема Вашего вопроса'
            }),
            "text": Textarea(attrs={
                'placeholder': 'Опишите Вашу проблему в деталях',
            })
        }
        