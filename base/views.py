from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
from matplotlib.style import context

# Create your views here.


rooms = [
    {'id':1, 'name': 'learning python'},
    {'id':2, 'name': 'learning javascript'},
    {'id':3, 'name': 'learning golang'},
]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request,'base/room.html', context) 