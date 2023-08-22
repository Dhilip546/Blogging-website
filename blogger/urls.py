from django.urls import path
from . import views

urlpatterns =[
    path('login/',views.index,name='index'),
    path('main/',views.main,name='main'),
]
