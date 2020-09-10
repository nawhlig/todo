from django import forms
from .models import Students


# 폼에 입력되는 데이터의 유효성검사 : ##### valid-ator ##### 기능
# 장고 폼에서는 forms에 기능함수를 만들지만
# 모델 폼에서는 models에 기능을 만듬
# 1. 검사기능을 만든다.
# 2. 장고 폼 형식에 가서 해당데이터 필드안에 validators=[메소드, 메소드, 메소드...] 라고 리스트형식으로 적용
# 3. 당연히 DB에 데이터 전달을 위해 VIEW에 가서 POST 방식으로도 작성

# [validation 방법 실습] 1.입력된 글자가 3글자 인지 검사 하고 메시지 출력하는 기능을 만듦
def min_length_3(value):  # value 로 들어온 값에대해 검사를 하자!
    if len(value) < 3:
        raise forms.ValidationError("3글자 이상 입력해주세요")  # raise로 오류를 발생시키자!


# 장고 폼 형식
class StudentForm(forms.Form):
    # [validation 방법 실습] 2. 만들어논 검사기능을 validators를 이용해 name에 적용 하고 view 로 이동
    name = forms.CharField(initial="initial='홍길동'하면 기본값", label="이름", validators=[min_length_3])
    address = forms.CharField(max_length=10)
    email = forms.CharField(widget=forms.Textarea)


# 모델 폼 형식
# models.py 에 만든 모델을 기반으로 자동으로 폼을 만듦(from .models import 모델) 필요함
class StudentModelForm(forms.ModelForm):
    # 내부 클래스 class Meta 빼먹으면 Model form has no model 오류 남, 문법임!
    class Meta:
        model = Students  # 어떤 모델을 할 껀지?
        fields = "__all__"  # 어떤 필드를 입력 받을 것 인지? ('__all__' 하면 전부 다)
        # fields = ["name", "address"]  # 두개의 필드만 폼만들고 입력받겠다는 의미
        labels = {"name": "이름"}  # 라벨 이름 영어 → 한글로
        help_texts = {"name": "이름을 입력해 주세요"}  # 입력창 아래 도움말 넣기
