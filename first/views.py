from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt  # csrf 보안
from django.http import HttpResponse, Http404
from django.utils import timezone
from .models import Students, Scores

# 폼사용 메소드 호출 define (StudentForm 은 장고폼,  StudentModelForm은 모델폼)
from .forms import StudentForm, StudentModelForm


# Create your views here.
# 템플릿한테 보내주기 = render 설명 :  1.request    2.템플릿경로 text 방식    3.보낼데이터 딕셔너리 형태로


@csrf_exempt
def index(request):
    return render(request, "first/index.html")


def students(request):
    students = Students.objects.all()  # 디비에서 데이터가져와서   # SELECT * FROM students 의 의미
    return render(
        request,
        "first/students.html",
        {"text": "안녕하세요!", "date": timezone.localtime(), "students": students},
    )  # 템플릿한테 보내주기


def students_detail(request, id):
    student = Students.objects.get(pk=id)  # 디비에서 데이터가져와서  # SELECT * FROM students 에서 id로 조회의미
    return render(request, "first/students_detail.html", {"student": student})  # 템플릿한테 보내주기


# 모델 폼 사용코드 (모델에 입력된 데이터 수정하는 기능)
def student_modify(request, id):
    # 수정할 id 값이 없을 때 처리 (페이지 없음 보여주기: 방법1)
    # try:
    #     student = Students.objects.get(pk=id)  # 디비에서 데이터가져와서
    # except:
    #     raise Http404("수정할 데이터가 없습니다.")

    # 수정할 id 값이 없을 때 처리 (페이지 없음 보여주기: 방법2)
    student = get_object_or_404(Students, pk=id)  # 디비에서 데이터가져와서

    if request.method == "GET":  # 브라우저에서 get으로 요청하면
        form = StudentModelForm(instance=student)  # 폼에 데이터 전달
        return render(request, "first/student_modify.html", {"form": form})

    elif request.method == "POST":  # 브라우저에서 post 로 전달하면
        form = StudentModelForm(request.POST, request.FILES, instance=students)
        if form.is_valid():
            form.save()  # 모델에 연관된 폼이라 바로 저장이 가능하다
            return redirect("first:students")
        else:  # 검사가 잘 안된경우 원래의 폼을 forms에 정의한 기능의 에러메시지와 함께 전달 ; 다시 폼으로 이동을 해라는 의미
            return render(request, "first/student_add.html", {"form": form})


# 모델 폼 사용코드 (모델에 데이터 입력하는 기능)
def student_add(request):
    if request.method == "GET":
        form = StudentModelForm()
        return render(request, "first/student_add.html", {"form": form})

    elif request.method == "POST":
        # 폼에서 데이터와 파일 업로드를 위해 request.POST, request.FILES 를 써준다.
        form = StudentModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()  # 모델에 연관된 폼이라 바로 저장이 가능하다
            return redirect("first:students")
        else:  # 검사가 잘 안된경우 원래의 폼을 forms에 정의한 기능의 에러메시지와 함께 전달 ; 다시 폼으로 이동을 해라는 의미
            return render(request, "first/student_add.html", {"form": form})


# 장고 폼 사용시 코드
#
# def student_add(request):
#     # 방법 1번
#     if request.method == "GET":
#         form = StudentForm() #장고폼 방식 선언
#         return render(request, "first/student_add.html", {"form": form})

#     elif request.method == "POST":
#         # [validation 방법 실습] 3. if form.is_valid() else 구문으로 입력되는 값을 보고 오류 메시지를 나오게 하자
#         # validator 적용을 위해 POST 방식 검사법도 작성
#         form = StudentForm(request.POST)
#         # 조건검사하는 부분 : forms에 작성산 조건(기능)들이 잘 돌아가는지 확인해줌
#         if form.is_valid():  # 검사가 잘 된경우 데이터를 폼에서 꺼내옴 ; 데이터를 입력해 준다는 의미
#             Students.objects.create(
#                 name=form.cleaned_data["name"],
#                 address=form.cleaned_data["address"],
#                 email=form.cleaned_data["email"],
#             )
#             return redirect("first:students")

#         else:  # 검사가 잘 안된경우 원래의 폼을 forms에 정의한 기능의 에러메시지와 함께 전달 ; 다시 폼으로 이동을 해라는 의미
#             return render(request, "first/student_add.html", {"form": form})

#         # Students.objects.create(
#         #     name=request.POST["name"], address=request.POST["address"], email=request.POST["email"]
#         # )
#         # return redirect("first:students")

#     # 방법 2번
#     # students = Students.objects.all()
#     # return render(request, 'first/students.html', {
#     #     'students': students
#     # })


def scores(request):
    scores = Scores.objects.all()  # 디비에서 데이터가져와서  # SELECT * FROM scores 의 의미
    return render(request, "first/scores.html", {"scores": scores})  # 템플릿한테 보내주기


def scores_add(request):
    # 방법 1번
    if request.method == "GET":
        return render(request, "first/scores_add.html")
    elif request.method == "POST":
        Scores.objects.create(
            name=request.POST["name"],
            math=request.POST["math"],
            english=request.POST["english"],
            science=request.POST["science"],
        )
        return redirect("first:scores")

    # 방법 2번
    # scores = Scores.objects.all()
    # return render(request, 'first/scores.html', {
    #     'students': scores
    # })


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


def make_cookie(request, name):
    res = HttpResponse()
    res.set_cookie("name", name)
    return res
