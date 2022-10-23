from django.shortcuts import render
from contact.forms import ContactForm
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


def sience(request):
    return render(request, 'nauka.html')

def profsouz(request):
    return render(request, 'profsouz.html')

def studsovet(request):
    return render(request, 'studsovet.html')
