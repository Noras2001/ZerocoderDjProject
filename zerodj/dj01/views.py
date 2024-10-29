from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse ('<h1>Hola Mundo!</h1>')
def datapage(request):
    return HttpResponse ('<h1>Data Page</h1>')

def testpage(request):
    return HttpResponse('<h1>Test Page</h1>')
