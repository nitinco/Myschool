from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    #return HttpResponse("hello welcome to my website")
    template = loader.get_template('test.html')
    return HttpResponse(template.render())
    
