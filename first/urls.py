from . import views
from django.urls import path, include

app_name = "first"

urlpatterns = [
    # path (url address "text format" , view function address&name , tag name "text format")
    path("", views.index, name="index"),
    path("students", views.students, name="students"),
    path("students/<int:id>", views.students_detail, name="students"),
    path("students/add", views.student_add, name="student_add"),
    path("students/modify/<int:id>", views.student_modify, name="student_modify"),
    path("scores", views.scores, name="scores"),
    path("sscores/add", views.scores_add, name="scores_add"),
    path("makecookie/<name>", views.make_cookie, name="make_cookie"),
]