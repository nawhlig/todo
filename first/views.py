from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Students, Scores


# Create your views here.
def index(request):
    return render(request, "first/index.html")


def students(request):
    # 디비에서 데이터가져와서
    students = Students.objects.all()  # SELECT * FROM students 의 의미
    # 템플릿한테 보내주기
    return render(
        request,
        "first/students.html",
        {"text": "안녕하세요!", "date": timezone.localtime(), "students": students},
    )


def students_detail(request, id):
    # 디비에서 데이터가져와서
    student = Students.objects.get(pk=id)  # SELECT * FROM students 에서 seq로 번호 의미
    # 템플릿한테 보내주기
    return render(request, "first/students_detail.html", {"student": student})


def scores(request):
    # 디비에서 데이터가져와서
    scores = Scores.objects.all()  # SELECT * FROM scores 의 의미
    # print(scores)  #DB에서 데이터 잘 가져오는지 확인

    # 템플릿한테 보내주기
    # render 설명 :  1.request    2.템플릿경로 text 방식    3.보낼데이터 딕셔너리 형태로
    return render(request, "first/scores.html", {"scores": scores})
