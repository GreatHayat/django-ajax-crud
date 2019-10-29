from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_list, name="index"),
    path("book_create", views.book_create, name="book_create")
]
