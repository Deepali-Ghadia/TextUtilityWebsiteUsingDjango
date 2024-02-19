from django.http import HttpResponse

def home(request):
    return HttpResponse("You are on the home page...")

def capitalize(request):
    return HttpResponse("<html><h1>Capitalize</h1><br><a href='/home'>BACK</a></html>")

def upper(request):
    return HttpResponse("<html><h1>Uppercase</h1><br><a href='/home'>BACK</a></html>")

def lower(request):
    return HttpResponse("<html><h1>Lowercase</h1><br><a href='/home'>BACK</a></html>")

def trim(request):
    return HttpResponse("<html><h1>Trim</h1><br><a href='/home'>BACK</a></html>")