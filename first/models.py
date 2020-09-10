from django.db import models
from django import forms  # 유효성 검사와 모델폼을 쓰기 위해서 forms 호출

# 모델 폼에서의 유효성검사 는 여기서!!! 정의하고
# 모델 클래스에 필드 뒤에 메소드 추가
def min_length_3(value):  # value 로 들어온 값에대해 검사를 하자!
    if len(value) < 3:
        raise forms.ValidationError("3글자 이상 입력해주세요")  # raise로 오류를 발생시키자!


# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=10, validators=[min_length_3])
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)


class Scores(models.Model):
    name = models.CharField(max_length=10)  # CharField 는 무조건 max_Length 그래야 자동으로 DB에서 결정
    math = models.IntegerField()
    english = models.IntegerField()
    science = models.IntegerField()