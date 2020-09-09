from . import views
from django.urls import path, include

app_name = "second"

urlpatterns = [
    # path (url address "text format" , view function address&name , tag name "text format")
    path("", views.index, name="index"),
    path("favourite", views.favourite, name="favourite"),
    path("favourite/<int:id>", views.favourite_detail, name="favourite"),
    path("todo", views.todo, name="todo"),
    path("todo/<int:id>", views.todo_detail, name="todo"),
]