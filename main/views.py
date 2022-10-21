
from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from blog.models import Blog


def index(request):

    blogs = Blog.objects.order_by('-date')

    error = ''

    form = ContactForm()
    context = {
        'blogs':blogs,
        'form': form,
        'error': error
    }

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была неверной'

    return render(request, 'index.html', context)


