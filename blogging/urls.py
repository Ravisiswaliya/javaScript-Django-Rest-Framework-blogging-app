from django.urls import path
from . import views

app_name = 'blogging'
urlpatterns = [
    path('', views.index, name='home'),
]