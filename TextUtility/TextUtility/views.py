from django.http import HttpResponse

def home(request):
    return HttpResponse("You are on the home page...")

def capitalize(request):
    return HttpResponse("First character of your text will be capitalized")

def upper(request):
    return HttpResponse("Input string will be converted to uppercase")

def lower(request):
    return HttpResponse("Input string will be converted to lowercase")

def trim(request):
    return HttpResponse("Leading and trailing whitespaces will be removed from the string")