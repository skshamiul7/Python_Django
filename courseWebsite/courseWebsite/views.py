from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def courses(request):
    return render(request, 'courses.html')


def FT(request):
    result = 0
    try:
        n1=int(request.GET['num1'])
        n2=int(request.GET['num2'])
        result = n1 + n2
    except:
        pass
    return render(request, 'FT.html', {'result': result})
