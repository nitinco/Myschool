from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    #return HttpResponse("hello welcome to my website")
    context={
        "topic":"neharu public school",
    }
    return render(request, 'test.html', context)
    
    
