from django.db import models
from django import forms  # 유효성 검사와 모델폼을 쓰기 위해서 forms 호출


# 모델 폼에서의 유효성검사 는 여기서!!! 정의하고
# 모델 클래스에 필드 뒤에 메소드 추가
def min_length_3(value):  # value 로 들어온 값에대해 검사를 하자!
    if len(value) < 3:
        raise forms.ValidationError("3글자 이상 입력해주세요")  # raise로 오류를 발생시키자!


# Create your models here.


class FavouriteGroup(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Favourite(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    memo = models.TextField()
    reg_date = models.DateField(auto_now_add=True)
    group = models.ForeignKey(FavouriteGroup, on_delete=models.CASCADE)


class TodoGroup(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now_add=True)
    del_yn = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Todo(models.Model):
    STATUS_CHOICES = (("pending", "할 일"), ("inprogress", "진행중"), ("end", "완료"))  # 상태 항목을 셀렉트 박스로 변경
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, validators=[min_length_3])
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    reg_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    del_yn = models.BooleanField(default=False)
    group = models.ForeignKey(TodoGroup, on_delete=models.CASCADE)
