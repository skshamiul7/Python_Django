from django.http import HttpResponse
from django.shortcuts import render

def getform(request):
    finalans = 0
    try:
        if request.method=='GET':
            n1 = int(request.GET.get('num1', ''))
            n2 = int(request.GET.get('num2', ''))
        finalans = n1 + n2
    except (TypeError, ValueError):
        pass
    return render(request, "get_form.html", {'output': finalans})

def postform(request):
    finalans = 0
    try:
        if request.method=='POST':
            n2 = int(request.POST.get('num2', ''))
            n1 = int(request.POST.get('num1', ''))
        finalans = n1 + n2
    except (TypeError, ValueError):
        pass
    return render(request, "post_form.html", {'output': finalans})

def userform(request):
    ans=0
    try:
        if request.method=="GET":
            n1=request.GET.get('name','')
            n2=request.GET.get('student_id','')
            n3=request.GET.get('university','')
            n4=request.GET.get('passing_year','')
            n5=request.GET.get('degree','')
            n6=request.GET.get('department','')
            n7=request.GET.get('cgpa','')
            n8=request.GET.get('email','')
            n9=request.GET.get('comments','')
        ans=n1+n2+n3+n4+n5+n6+n7+n8+n9
    except (TypeError, ValueError):
        pass
    return render (request, "get.html", {'output': ans})