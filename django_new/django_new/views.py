

from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, 'about.html',{'gret': 'Hello,World'})


def home(request):
    return HttpResponse('This is my home')