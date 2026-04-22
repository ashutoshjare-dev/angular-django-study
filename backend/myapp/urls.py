# backend/myapp/urls.py
from django.urls import path
from myapp import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
]