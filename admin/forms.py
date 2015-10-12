from django import forms

from django.forms import ModelForm, TextInput
from django.forms.widgets import RadioChoiceInput

from lesson.models import Course
from word.models import Word, Language, Question

__author__ = 'FRAMGIA\nguyen.huy.quyet'


class CreateCourseViewForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'content']
        widgets = {
            'name': TextInput(attrs={'cols': 30, 'rows': 1}),
            'content': TextInput(attrs={'cols': 30, 'rows': 3}),
        }


class CreateWordViewForm(forms.ModelForm):
    language = forms.ModelChoiceField(queryset=Language.objects.all())

    class Meta:
        model = Word
        fields = ['name', 'meaning', 'language']

#
# class CreateQuestionWordView(ModelForm):
#     class Meta:
#         model = Question
#         fields = ['answer', 'check']
#         widgets = {
#             'name': TextInput(attrs={'cols': 30, 'rows': 1}),
#             'check': RadioChoiceInput(attrs={'cols': 30, 'rows': 3}),
#         }
