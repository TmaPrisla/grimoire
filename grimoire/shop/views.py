from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': 'О нас', 'url_name' : 'about'},
        {'title': 'Футболки', 'url_name' : 'shirts'},
        {'title': 'Худи', 'url_name' : 'hodies'},
        {'title': 'Джогеры', 'url_name' : 'djogers'},
        {'title': 'Корзина', 'url_name' : 'home'},
]


def index(request):
    posts = Futbolki.objects.all()
    context = {'posts': posts,
               "menu": menu,
               'title': 'Главная страница'
    }

    return render(request, 'shop/index.html', context=context)


def about(request):
    return render(request, 'shop/about.html', {'title': 'О сайте',"menu": menu})


def shirts(request):
    posts = Futbolki.objects.filter(title__contains='Футболка')
    context = {'posts': posts,
               "menu": menu,
               'title': 'Shirts'
               }
    return render(request, 'shop/shirts.html', context= context)


def hodies(request):
    posts = Futbolki.objects.filter(title__contains='Hoodie')
    context = {'posts': posts,
               "menu": menu,
               'title': 'Hoodies'
               }

    return render(request, 'shop/hodies.html', context=context)


def djogers(request):
    posts = Futbolki.objects.filter(title__contains='Джогеры')
    context = {'posts': posts,
               "menu": menu,
               'title': 'Djogers'
               }
    return render(request, 'shop/djogers.html', context=context)


def productpage(request, catid):
    w1 = Futbolki.objects.get(path=catid)
    return render(request, 'shop/catalogitems.html', {'title': w1.title, 'content': w1.content, 'img': w1.photo, 'price': w1.price ,'menu': menu})


def catalog(request):
    posts = Futbolki.objects.all()
    return render(request, 'shop/pizda.html', {'posts': posts, 'title': 'catalog',"menu": menu})


def pagenotfound(requset, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
