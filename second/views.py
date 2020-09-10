from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt  # csrf 보안
from django.http import HttpResponse, Http404
from .models import Favourite, Todo  # 모델 호출 define
from .forms import FavouriteModelForm, TodoModelForm  # 모델 폼사용 메소드 호출 define


@csrf_exempt
def index(request):
    return render(request, "second/index.html")


def favourite(request):
    # 디비에서 데이터가져와서
    db_favourite_all = Favourite.objects.all()  # SELECT * FROM Favourite 의 의미
    # 템플릿한테 보내주기
    return render(
        request, "second/favourite.html", {"text": "즐겨찾기", "views_favourites": db_favourite_all}
    )


def favourite_detail(request, id):
    # 디비에서 데이터가져와서
    db_favourite = Favourite.objects.get(pk=id)
    # 템플릿한테 보내주기
    return render(request, "second/favourite_detail.html", {"views_favourite": db_favourite})


# 모델 폼 사용시 코드
def favourite_add(request):
    if request.method == "GET":
        form = FavouriteModelForm()
        return render(request, "second/favourite_add.html", {"form": form})

    elif request.method == "POST":
        form = FavouriteModelForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save()  # 모델에 연관된 폼이라 바로 저장이 가능하다
            return redirect("second:favourite")
        else:  # 검사가 잘 안된경우 원래의 폼을 forms에 정의한 기능의 에러메시지와 함께 전달 ; 다시 폼으로 이동을 해라는 의미
            return render(request, "second/favourite_add.html", {"form": form})


# 모델 폼 사용코드 (모델에 입력된 데이터 수정하는 기능)
def favourite_modify(request, id):
    # 수정할 id 값이 없을 때 처리 (페이지 없음 보여주기: 방법1)
    try:
        db_favourite = Favourite.objects.get(pk=id)  # 디비에서 데이터가져와서
    except:
        raise Http404("수정할 데이터가 없습니다.")

    # 수정할 id 값이 없을 때 처리 (페이지 없음 보여주기: 방법2)
    # student = get_object_or_404(Students, pk=id)  # 디비에서 데이터가져와서

    if request.method == "GET":  # 브라우저에서 get으로 요청하면
        form = FavouriteModelForm(instance=db_favourite)  # 폼에 데이터 전달
        return render(request, "second/favourite_modify.html", {"form": form})

    elif request.method == "POST":  # 브라우저에서 post 로 전달하면
        form = FavouriteModelForm(request.POST, instance=db_favourite)
        if form.is_valid():
            form.save()  # 모델에 연관된 폼이라 바로 저장이 가능하다
            return redirect("second:favourite")
        else:  # 검사가 잘 안된경우 원래의 폼을 forms에 정의한 기능의 에러메시지와 함께 전달 ; 다시 폼으로 이동을 해라는 의미
            return render(request, "second/favourite_add.html", {"form": form})


def favourite_delete(request, id):
    # 수정할 id 값이 없을 때 처리 (페이지 없음 보여주기: 방법1)
    try:
        db_favourite = Favourite.objects.get(pk=id)  # 디비에서 데이터가져와서
    except:
        raise Http404("삭제할 데이터가 없습니다.")

    db_favourite.delete()
    return redirect("second:favourite")
    # 수정할 id 값이 없을 때 처리 (페이지 없음 보여주기: 방법2)
    # student = get_object_or_404(Students, pk=id)  # 디비에서 데이터가져와서

    # if request.method == "GET":  # 브라우저에서 get으로 요청하면
    #     return redirect("second:favourite")

    # elif request.method == "POST":  # 브라우저에서 post 로 전달하면
    #     db_favourite.delete()
    #     return redirect("second:favourite")


def todo(request):
    # DB 데이터 추출
    db_todo = Todo.objects
    # if "group" in request.GET:
    #     db_todo = Todo.objects.filter(group__name=request.GET["group"])

    # if "end_date" in request.GET:
    #     db_todo = Todo.objects.filter(end_date__gte=request.GET["end_date"])

    # 템플릿한테 보내주기
    # render 설명 :  1.request    2.템플릿경로 text 방식    3.보낼데이터 딕셔너리 형태로
    return render(
        request,
        "second/todo.html",
        {
            "text": "내가 할 일",
            "views_todo_pending": db_todo.filter(status="pending").order_by("end_date"),
            "views_todo_inprogress": db_todo.filter(status="inprogress").order_by("end_date"),
            "views_todo_end": db_todo.filter(status="end").order_by("end_date"),
        },
    )


def todo_detail(request, id):
    # 디비에서 데이터가져와서
    db_todo_detail = Todo.objects.get(pk=id)
    # 템플릿한테 보내주기
    return render(request, "second/todo_detail.html", {"views_todo": db_todo_detail})


def todo_add(request):
    if request.method == "GET":
        form = TodoModelForm()
        return render(request, "second/todo_add.html", {"form": form})

    elif request.method == "POST":
        form = TodoModelForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()  # 모델에 연관된 폼이라 바로 저장이 가능하다
            return redirect("second:todo")
        else:  # 검사가 잘 안된경우 원래의 폼을 forms에 정의한 기능의 에러메시지와 함께 전달 ; 다시 폼으로 이동을 해라는 의미
            return render(request, "second/todo_add.html", {"form": form})


# 모델 폼 사용코드 (모델에 입력된 데이터 수정하는 기능)
def todo_modify(request, id):
    # 수정할 id 값이 없을 때 처리 (페이지 없음 보여주기: 방법1)
    try:
        db_todo = Todo.objects.get(pk=id)  # 디비에서 데이터가져와서
    except:
        raise Http404("수정할 데이터가 없습니다.")

    # 수정할 id 값이 없을 때 처리 (페이지 없음 보여주기: 방법2)
    # student = get_object_or_404(Students, pk=id)  # 디비에서 데이터가져와서

    if request.method == "GET":  # 브라우저에서 get으로 요청하면
        form = TodoModelForm(instance=db_todo)  # 폼에 데이터 전달
        return render(request, "second/todo_modify.html", {"form": form})

    elif request.method == "POST":  # 브라우저에서 post 로 전달하면
        form = TodoModelForm(request.POST, instance=db_todo)
        if form.is_valid():
            form.save()  # 모델에 연관된 폼이라 바로 저장이 가능하다
            return redirect("second:todo")
        else:  # 검사가 잘 안된경우 원래의 폼을 forms에 정의한 기능의 에러메시지와 함께 전달 ; 다시 폼으로 이동을 해라는 의미
            return render(request, "second/todo_add.html", {"form": form})


def todo_delete(request, id):
    # 수정할 id 값이 없을 때 처리 (페이지 없음 보여주기: 방법1)
    try:
        db_todo = Todo.objects.get(pk=id)  # 디비에서 데이터가져와서
    except:
        raise Http404("삭제할 데이터가 없습니다.")

    db_todo.delete()
    return redirect("second:todo")