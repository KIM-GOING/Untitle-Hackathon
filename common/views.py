from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request) :
    return render(request, 'common/base.html')

def letter(request) :
    return render(request, 'letter/letter.html')