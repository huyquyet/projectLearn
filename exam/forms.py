from django import forms
from exam.models import Answer

from word.models import Word, Question

__author__ = 'FRAMGIA\nguyen.huy.quyet'


class AnswerForms(forms.Form):
    # CHOICES = (
    #     (1, 'Regular Service'),
    #     (0, 'Premium Service')
    # )
    # answer_1 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'Radio'}), initial=1)
    # question_1 = forms.ModelChoiceField(queryset=Word.objects.question.all().values_list('answer'),
    #                                     widget=forms.RadioSelect(attrs={'class': 'Radio'}), initial=1)
    # a = Word.objects.question.ALL()

    class Meta:
        model = Word
        fields = ['name', 'question']

        # def __init__(self, *args, **kwargs):
        #
        #     super(AnswerForms, self).__init__(*args, **kwargs)


class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['name']


class AnswerForm(forms.ModelForm):
    question = forms.ModelChoiceField(queryset=Question.objects.all(), widget=forms.RadioSelect(attrs={'class': 'Radio'}))

    class Meta:
        model = Answer
        fields = ['question']

    def __init__(self, *args, **kwargs):
        self.word = kwargs.get('word', None)
        super().__init__(*args, **kwargs)
        queryset = kwargs.get('queryset', None)
        if queryset is not None:
            self.question.queryset = kwargs.pop('questions', )
