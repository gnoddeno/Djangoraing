from django.contrib import admin
from django.urls import path

from .views import getUser, postUser, update, delete, createUser

urlpatterns = [
    path('get/', getUser),
    path('post/', postUser),
    path('create/', createUser),
    path('update/<str:name>/', update),
    path('delete/<str:name>/', delete),
]
