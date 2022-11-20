from django.shortcuts import render
import random

# Create your views here.

def index(request) :
    return render(request, 'santa/make_santa.html')
    '''
    x = random.randint(1, 3)
    if x == 1 :
        return render(request, 'santa/make_santa.html')
    elif x == 2 :
        return render(request, 'santa/make_santa_small.html')
    elif x == 3 :
        return render(request, 'santa/make_santa_big.html')
    '''

def adult(request) :
    return render(request, 'santa/finish_santa.html')

def finish(request) :
    return render(request, 'common/santafi.html')