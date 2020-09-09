from django.shortcuts import render
from django.http import HttpResponse
from .models import Favourite, Todo


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


# 쿼리 실습문제
# name에 외식이 들어가 있는 할 일을 검색
# Todo.objects.filter(name__contains='외식').values()

# 종료날짜가 3월에 있는 할일을 검색해주세요
# Todo.objects.filter(end_date__gte='2020-03-01',end_date__lte='2020-03-31').values()

# 현재 공부중 inprogress 상태인 것들을 검색해주세요
# Todo.objects.filter(group__name='공부',status='inprogress').values()

# 현재 공부나 가족중 완료된것들을 검색해주세요
# Todo.objects.filter((Q(group__name='공부') | Q(group__name='가족')) & Q(status='end')).values()
# Todo.objects.filter(Q(group__name='공부') | Q(group__name='가족')).filter(status='end').values()

# 현재 공부인 항목들을 종료날짜기준 내림차순으로 정렬해주세요
# Todo.objects.filter(group__name='공부').order_by('-end_date').values()


# 실습문제
# python manage.py shell
# second.models form Todo
# second.models form TodoGroup
# TodoGroup.objects.all().values()
# Todo.objects.create(name='어머니생신',status='pending',end_date='2020-10-07',group_id=1)
# Todo.objects.create(name='아버지생신',status='end',end_date='2020-03-07',group_id=1)
# Todo.objects.create(name='가족외식',status='pending',end_date='2020-11-07',group_id=1)
# Todo.objects.create(name='가족외식',status='end',end_date='2020-03-07',group_id=1)
# Todo.objects.create(name='SQL',status='end',end_date='2020-08-24',group_id=2)
# Todo.objects.create(name='웹프로그래밍기초',status='end',end_date='2020-08-30',group_id=2)
# Todo.objects.create(name='Django',status='inprogress',end_date='2020-09-06',group_id=2)
# Todo.objects.create(name='React',status='inprogress',end_date='2020-09-15',group_id=2)
# Todo.objects.create(name='회사이사',status='pending',end_date='2020-10-20',group_id=3)
# Todo.objects.all().values()

# 장고 쉘에서 ORM 이용방법
# 추가
# Favourite.objects.create(name='네이버2',url='https://naver.com',memo='Memo',group_id=2)
# favourite = Favourite()
# favourite.name = '네이버3'
# favourite.url = 'https://naver.com'
# favourite.memo = '메모3'
# favourite.group_id = 1
# favourite.save()
# Favourite.objects.all().values()
# 수정
# favourite = Favourite.objects.get(pk=4)
# favourite.name = '네이버2입니다'
# favourite.save()
# Favourite.objects.all().values()
# 삭제
# favourite = Favourite.objects.get(pk=4)
# favourite.delete()