from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def capitalize(request):
    print("\n\n",request.GET.get("input_text","default"))
    received_text = request.GET.get("input_text","default") # collect the data that is passed to input_text i.e. textarea
    modified_text = received_text.capitalize()
    print("MODIFIED TEXT",modified_text)
    params = {'modified_text':modified_text}
    return render(request,"capitalize.html",params)

def upper(request):
    received_text = request.GET.get('input_text')
    modified_text = received_text.upper()
    params = {"modified_text":modified_text}
    return render(request,'upper.html',params)

def lower(request):
    return HttpResponse("<html><h1>Lowercase</h1><br><a href='/home'>BACK</a></html>")

def trim(request):
    return HttpResponse("<html><h1>Trim</h1><br><a href='/home'>BACK</a></html>")