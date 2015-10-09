from django.forms import ModelForm, Textarea, TextInput

from lesson.models import Course

__author__ = 'FRAMGIA\nguyen.huy.quyet'


class CreateCourseViewForm(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'content']
        widgets = {
            'name': TextInput(attrs={'cols': 30, 'rows': 1}),
            'content': TextInput(attrs={'cols': 30, 'rows': 3}),
        }
