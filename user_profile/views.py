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
from authentification.forms import UserRegistrationForm, UserLoginForm
from django.http.response import HttpResponse

from user_profile.models import Schedule
from user_profile.parser import parser

def profile(request):
    text = parser(request)
    return render(request, 'auth/profile.html', text)

def download_file(request):

    group = request.user.first_name
    BASE_DIR = Path(__file__).resolve().parent.parent
    base_str = str(BASE_DIR)

    filename = group+'.xlsx'
    # Define the full file path
    filepath = base_str + "\\schedule\\" + filename
    print(filepath)
    
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response

def parsed_page(request):
    text = parser(request)
    return render(request, 'profile/parsed.html', text)