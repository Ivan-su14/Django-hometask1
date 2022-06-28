from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('General page')

def about(request):
    return HttpResponse('<h1>Hello world this is About page</h1><br><p>Это страница about</p>')

def contacts(request):
    return HttpResponse('<h1>This is contacts page.</h1><br><p>Звоните мне в любое время 777-77-77</p>')