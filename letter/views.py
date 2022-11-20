from django.shortcuts import render, redirect
from letter.models import Letters

# Create your views here.

def index(request) :

    letterlist = Letters.objects.all()

    return render(request, 'letter/letter.html', {'letterlist':letterlist})

def new_letter(request) :
    if request.method == 'POST' :
        letter = Letters.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
        )

        return redirect('/santa/finish/')

    return render(request, 'letter/new_letter.html')