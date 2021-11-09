from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('shirts/', shirts, name='shirts'),
    path('hodies/', hodies, name='hodies'),
    path('djogers/', djogers, name='djogers'),
    path('catalog/<slug:catid>/', productpage, name='catid'),
    path('catalog/', catalog, name='catalog')
]
