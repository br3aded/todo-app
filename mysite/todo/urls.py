from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('home', views.home, name='home'),
]