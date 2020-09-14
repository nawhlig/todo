from django.urls import path, include
from . import views


app_name = "second"

urlpatterns = [
    # path (url address "text format" , view function address&name , tag name "text format")
    path("", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("signin/ok", views.signin_ok, name="signin_ok"),
    path("signout", views.signout, name="signout"),
    path("index", views.index, name="index"),
    path("favourite", views.favourite, name="favourite"),
    path("favourite/<int:id>", views.favourite_detail, name="favourite_detail"),
    path("favourite/add", views.favourite_add, name="favourite_add"),
    path("favourite/modify/<int:id>", views.favourite_modify, name="favourite_modify"),
    path("favourite/delete/<int:id>", views.favourite_delete, name="favourite_delete"),
    path("todo", views.todo, name="todo"),
    path("todo/<int:id>", views.todo_detail, name="todo_detail"),
    path("todo/add", views.todo_add, name="todo_add"),
    path("todo/modify/<int:id>", views.todo_modify, name="todo_modify"),
    path("todo/delete/<int:id>", views.todo_delete, name="todo_delete"),
]