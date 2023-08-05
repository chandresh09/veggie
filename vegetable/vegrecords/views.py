from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

# Create your views here.
def index(request):
    return HttpResponse('This is vegetable project')


def vegetable(request):
    a=[
        {'name':'potato','type':'a','quantity':10},
        {'name':'tomato','type':'b','quantity':20},
        {'name':'onion','type':'a','quantity':0},
        {'name':'carrot','type':'c','quantity':5},
        {'name':'garlic','type':'a','quantity':0},
    ]
    print(a)
    return render(request,'vegetables.html',{'v1':a})

def create(request):
    if request.method== 'POST':
        f=vegform(request.POST)
        if f.is_valid():
            print('Form is valid')
            try:
                f.save()
                return HttpResponse('Form is submitted')
             #   return redirect('/vegetable')
            except:
                pass
        else:
            pass
    else:
        f=vegform()
    return render(request,'create.html',{'form':f})