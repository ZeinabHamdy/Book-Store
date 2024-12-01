from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(req):
    return HttpResponse('Welcome in Store Page...')

def ourStore(req):
    return render(req, 'store/index.html',
    {'name' : 'zainab hamdy ali hassan',
    'age' : 21,
    })