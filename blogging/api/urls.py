from django.urls import path, include
from . import views
from rest_framework import routers


app_name = 'blog-api'
urlpatterns = [
    path('allpost/', views.PostView.as_view(), name='allpost'),
    path('post/<int:pk>', views.SinglePostView.as_view(), name='post-detail')
]