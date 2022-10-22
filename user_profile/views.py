from django.shortcuts import render
from pathlib import Path
import mimetypes
from django.http.response import HttpResponse
from user_profile.parser import parser


def profile(request):
    text = parser(request)
    return render(request, 'auth/profile.html', text)


def download_file(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    base_str = str(BASE_DIR)
    filename = 'schedule.xlsx'
    filepath = base_str + "\\schedule\\" + 'schedule.xlsx'
    print(filepath)
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def parsed_page(request):
    text = parser(request)
    return render(request, 'profile/parsed.html', text)
    