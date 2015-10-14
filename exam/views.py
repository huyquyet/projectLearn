# import datetime
from django.core.urlresolvers import reverse_lazy

from django.forms import formset_factory


# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from exam.forms import AnswerForms, AnswerForm
from exam.models import Exam
from lesson.models import Lesson, LessonUser


def UserLessonExamView_1(request):
    # model = Question
    exam_forms = formset_factory(AnswerForms)
    data = {
        'form-TOTAL_FORMS': '2',
        'form-INITIAL_FORMS': '0',
        'form-MIN_NUM_FORMS': '',
        'form-MAX_NUM_FORMS': '',
        'form-0-title': 'Test',
        'form-0-pub_date': '1904-06-16',
        'form-1-title': 'Test 2',
        'form-1-pub_date': '1912-06-23',
    }
    # formset = exam_forms
    #
    # template_name = 'exam/user/exam_lesson.html'
    if request.method == 'POST':
        a = exam_forms(data, request.POST, request.FILES)
        if a.is_valid():
            # do something with the formset.cleaned_data
            pass
    else:
        a = exam_forms()
    return render_to_response('exam/user/exam_lesson.html', {'formset': a})


class UserLessonExamView(SingleObjectMixin, FormView):
    model = Lesson
    template_name = 'exam/user/exam_lesson.html'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        extra = self.object.word.count()
        self.form_class = formset_factory(AnswerForm, extra=extra)
        return super(UserLessonExamView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(UserLessonExamView, self).get_form_kwargs()
        return kwargs

    def get_form(self, form_class=None):
        formset = super(UserLessonExamView, self).get_form(form_class)
        words = self.object.word.all()
        for (form, word) in list(zip(formset, words)):
            form.word = word
            form.fields['question'].queryset = word.question.all().
        return formset

    def form_valid(self, form):
        lession_user = get_object_or_404(LessonUser, user=self.request.user, lesson=self.object)
        exam = Exam.objects.create(lesson_user=lession_user)
        exam.save()
        for frm in form:
            answer = frm.save(commit=False)
            answer.exam = exam
            answer.save()
        return super(UserLessonExamView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('lesson:lesson-detail', kwargs={'pk': self.object.pk})
