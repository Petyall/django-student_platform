from contact.models import Contact
from django.forms import ModelForm, TextInput, Textarea


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone_number", "theme", "text"]
        widgets = {
            "name": TextInput(attrs={
                'class':'form-control'
            }),
            "email": TextInput(attrs={
                'class':'form-control'
            }),
            "phone_number": TextInput(attrs={
                'class':'form-control'
            }),
            "theme": TextInput(attrs={
                'class':'form-control'
            }),
            "text": Textarea(attrs={
                'class':'form-control'
            })
        }
