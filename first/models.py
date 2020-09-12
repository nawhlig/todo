from django.db import models
from django import forms  # 유효성 검사와 모델폼을 쓰기 위해서 forms 호출
from uuid import uuid4  # 유니크한 id 생성해주는 함수 호출 (웹→DB업로드시 파일명 겹치지 않게)
import os

# 모델 폼에서의 유효성검사 는 여기서!!! 정의하고
# 모델 클래스에 필드 뒤에 메소드 추가
def min_length_3(value):  # value 로 들어온 값에대해 검사를 하자!
    if len(value) < 3:
        raise forms.ValidationError("3글자 이상 입력해주세요")  # raise로 오류를 발생시키자!


# 업로드하는 파일명과 경로를 마음대로 지정할 수 있게 한다
def upload_to(instance, filename):
    path = "file"

    uuid_name = uuid4().hex  # 파일명을 랜덤값(# 길이 32 인 uuid 값)으로 뽑고
    # 파일명에서 확장자 떨어짐 : 확장자 구하기 방법1 - os 기능을 이용
    extension = os.path.splitext(filename)[-1].lower()
    # 파일명에서 확장자 떨어짐 : 확장자 구하기 방법2 - 스플릿으로 구분해서
    # filename.split(".")[-1]
    # return "/" + path + uuid_name + extension  # 위아래 똑같음
    return "/".join(
        [
            path,
            uuid_name + extension,
        ]
    )


# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=10, validators=[min_length_3])
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    # 이미지 업로드 필드와 경로 지정
    file1 = models.FileField(null=True, blank=True, upload_to="")  # settings.py에 정의된 기본폴더 media로
    file2 = models.FileField(null=True, blank=True, upload_to=upload_to)  # def upload() 의 지정된 형식으로
    img1 = models.ImageField(null=True, blank=True, upload_to="images")  # images 폴더로
    img2 = models.ImageField(null=True, blank=True, upload_to="%Y/%m/%d")  # 2020\09\12 형식의 폴더로


class Scores(models.Model):
    name = models.CharField(max_length=10)  # CharField 는 무조건 max_Length 그래야 자동으로 DB에서 결정
    math = models.IntegerField()
    english = models.IntegerField()
    science = models.IntegerField()