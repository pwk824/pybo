from django import forms
from freebo.models import Freewriting
from freebo.models import Replying
from django_summernote.widgets import SummernoteWidget

class FreewritingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FreewritingForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['title'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })
    class Meta:
        model = Freewriting  # 사용할 모델
        fields = ['title', 'content']  # FreewritingForm에서 사용할 Freewriting 모델의 속성
        widgets = {
            'content': SummernoteWidget(),
        }
        labels = {
            'title': '제목',
            'content': '내용',
        }

class ReplyingForm(forms.ModelForm):
    class Meta:
        model = Replying
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }