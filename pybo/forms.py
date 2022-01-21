from django import forms
from pybo.models import Question
from pybo.models import Answer
from django_summernote.widgets import SummernoteWidget

class QuestionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['subject'].label = '제목'
        self.fields['subject'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        widgets = {
            'content': SummernoteWidget(),
        }
        labels = {
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = '내용'
        self.fields['content'].widget.attrs.update({
            'placeholder': '제목을 입력해주세요.',
            'class': 'form-control',
            'autofocus': True,
        })
    class Meta:
        model = Answer
        fields = ['content']
        widgets = {
            'content': SummernoteWidget(),
        }
        labels = {
            'content': '답변내용',
        }



