from django.urls import path
from . import views

urlpatterns=[
    path('',views.main,name='main'),
    path('add',views.add,name='add')
    
    ]