from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def capitalize(request):
    print("\n\n",request.POST.get("input_text"))
    received_text = request.POST.get("input_text") # collect the data that is passed to input_text i.e. textarea
    modified_text = received_text.capitalize()
    print("MODIFIED TEXT",modified_text)
    params = {'modified_text':modified_text}
    return render(request,"capitalize.html",params)

def upper(request):
    received_text = request.GET.get("input_text")
    modified_text = received_text.upper()
    params = {"modified_text":modified_text}
    return render(request,'upper.html',params)

def lower(request):
    received_text = request.GET.get("input_text")
    modified_text = received_text.lower()
    params = {"modified_text":modified_text}
    return render(request,'lowercase.html',params)

def trim(request):
    received_text = request.GET.get("input_text")
    modified_text = received_text.replace(" ","")
    params = {"modified_text":modified_text}
    return render(request,'trim.html',params)