# import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

from django.forms import formset_factory


# Create your views here.
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import FormView, DetailView, ListView
from django.views.generic.detail import SingleObjectMixin
from exam.forms import AnswerForm
from exam.models import Exam
from lesson.models import Lesson, LessonUser
from word.models import Word


class UserLessonExamView(SingleObjectMixin, FormView):
    model = Lesson
    template_name = 'exam/user/exam_lesson.html'
    # context_object_name = 'detail_'
    id_exam = 0

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        extra = self.object.word.count()
        self.form_class = formset_factory(AnswerForm, extra=extra)
        return super(UserLessonExamView, self).dispatch(request, *args, **kwargs)

    # def get_form_kwargs(self):
    #     kwargs = super(UserLessonExamView, self).get_form_kwargs()
    #     return kwargs

    def get_form(self, form_class=None):
        formset = super(UserLessonExamView, self).get_form(form_class)
        words = self.object.word.all()
        for (form, word) in list(zip(formset, words)):
            form.word = word
            form.fields['question'].queryset = word.question.all()
        return formset

    def form_valid(self, form):
        formset = form
        lession_user = get_object_or_404(LessonUser, user=self.request.user, lesson=self.object)
        exam = Exam.objects.create(lesson_user=lession_user)
        exam.save()
        self.id_exam = exam.pk
        count = 0
        for form in formset:
            answer = form.save(commit=False)
            answer.exam = exam
            question = form.cleaned_data['question']
            if question.check:
                word = Word.objects.get(id=question.word.id)
                if Word.objects.filter(user=self.request.user, pk=word.pk).exists():
                    pass
                else:
                    word.user.add(self.request.user)
                    word.save()
                count += 1
            answer.save()
        exam.point = count
        exam.save()
        return super(UserLessonExamView, self).form_valid(formset)

    def get_context_data(self, **kwargs):
        ctx = super(UserLessonExamView, self).get_context_data(**kwargs)

        return ctx

    def get_success_url(self):
        return reverse_lazy('exam:exam-history-detail', kwargs={'pk': self.id_exam})


class UserListHistoryExamView(ListView):
    model = Exam
    template_name = 'exam/user/exam_list_history.html'
    context_object_name = 'list_exam'

    def get_queryset(self):
        return Exam.objects.filter(lesson_user__user=self.request.user).select_related('lesson_user')
        # return super(UserListHistoryExamView, self).get_queryset()


class UserHistoryExamView(DetailView):
    model = Exam
    template_name = 'exam/user/exam_history_detail.html'
    context_object_name = 'exam_detail'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserHistoryExamView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(UserHistoryExamView, self).get_context_data(**kwargs)
        ctx['users'] = self.object.lesson_user.user
        answer = self.object.answer.all()
        ctx['answer'] = answer
        ctx['id_question'] = [i.question.id for i in answer]
        words = [i.question.word for i in answer]
        ctx['words'] = words
        # questions =
        return ctx