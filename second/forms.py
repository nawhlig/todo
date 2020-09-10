from django import forms
from .models import Favourite, Todo


# 모델 폼 형식
# models.py 에 만든 모델을 기반으로 자동으로 폼을 만듦(from .models import 모델) 필요함
class FavouriteModelForm(forms.ModelForm):
    # 내부 클래스 class Meta 빼먹으면 Model form has no model 오류 남, 문법임!
    class Meta:
        model = Favourite  # 어떤 모델을 할 껀지?
        fields = "__all__"  # 어떤 필드를 입력 받을 것 인지? ('__all__' 하면 전부 다)
        labels = {"name": "명칭", "Memo": "메모", "group": "그룹"}  # 라벨 이름 영어 → 한글로
        # help_texts = {"name": "이름을 입력해 주세요"}  # 입력창 아래 도움말 넣기


class TodoModelForm(forms.ModelForm):
    # 내부 클래스 class Meta 빼먹으면 Model form has no model 오류 남, 문법임!
    class Meta:
        model = Todo  # 어떤 모델을 할 껀지?
        fields = ["name", "status", "end_date", "group"]  # 어떤 필드를 입력 받을 것 인지? ('__all__' 하면 전부 다)
        labels = {"name": "할 일", "status": "상태", "end_date": "종료일", "group": "그룹"}  # 라벨 이름 영어 → 한글로
        # help_texts = {"name": "이름을 입력해 주세요"}  # 입력창 아래 도움말 넣기
