from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from lesson.models import Lesson, Course, LessonUser
from word.models import Word

__author__ = 'FRAMGIA\nguyen.huy.quyet'
requirement_admin = user_passes_test(lambda u: u.is_staff, login_url='admin:login-admin')


class AdminListLessonView(ListView):
    model = Lesson
    template_name = 'lesson/admin/admin_list_lesson.html'
    context_object_name = 'list_lesson'


class AdminCreateLessonView(CreateView):
    model = Lesson
    template_name = 'lesson/admin/admin_create_lesson.html'
    fields = ['name', 'content']

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminCreateLessonView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.course = Course.objects.get(id=self.request.session['course_id'])
        form.save()
        return super(AdminCreateLessonView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('admin:admin-detail-course', kwargs={'pk': self.request.session['course_id']})


class AdminEditLessonView(UpdateView):
    model = Lesson
    template_name = 'lesson/admin/admin_edit_lesson.html'
    fields = ['name', 'content']

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminEditLessonView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin:admin-detail-lesson', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        ctx = super(AdminEditLessonView, self).get_context_data(**kwargs)
        ctx['status'] = self.object.status
        return ctx

    def form_valid(self, form):
        status = self.request.POST.get('status', '')
        if status != '':
            if status:
                count = self.object.word.all().count()
                if count == 10:
                    form.instance.status = True
                form.save()
        else:
            form.save()
        return super(AdminEditLessonView, self).form_valid(form)


class AdminDetailLessonView(DetailView):
    model = Lesson
    template_name = 'lesson/admin/admin_detail_lesson.html'
    context_object_name = 'detail_lesson'

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminDetailLessonView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(AdminDetailLessonView, self).get_context_data(**kwargs)
        ctx['language'] = self.object.course.language.name
        # ctx['status'] = self.object
        word = self.object.word.all()
        num = word.count()
        if num >= 10:
            ctx['num'] = False
        else:
            ctx['num'] = True

        ctx['words'] = word
        ctx['users'] = self.object.user.all()
        return ctx


@requirement_admin
def admin_delete_lesson(request):
    id_lesson = request.POST.get('id_lesson', '')
    id_course = request.POST.get('id_course', '')
    if id_lesson == '':
        return render(request, 'lesson/admin/admin-delete-error.html',
                      {'error': 'Loi xoa Lesson', 'id_course': id_course})
    else:
        lesson = get_object_or_404(Lesson, id=id_lesson)
        if lesson.status:
            return render(request, 'lesson/admin/admin-delete-error.html',
                          {'error': 'Loi xoa Lesson', 'id_course': id_course})
        else:
            lesson.delete()
            return HttpResponseRedirect(reverse_lazy('admin:admin-detail-course', kwargs={'pk': id_course}))


class AdminAddWordLessonView(DetailView):
    model = Lesson
    template_name = 'lesson/admin/admin_add_word_lesson.html'
    context_object_name = 'detail_lesson'

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminAddWordLessonView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(AdminAddWordLessonView, self).get_context_data(**kwargs)
        words = self.object.word.all()
        # id language of lesson
        lang_lesson = self.object.course.language.id
        list_word_not_in_lesson = Word.objects.annotate(num_question=Count('question')).filter(
            language__id=lang_lesson, num_question=3).exclude(
            id__in=words)
        ctx['list_word'] = words
        ctx['count_word'] = words.count()
        ctx['list_word_not_in_lesson'] = list_word_not_in_lesson
        return ctx

        # def post(self, request, *args, **kwargs):
        #     pass


@requirement_admin
def add_word_lesson(request):
    id_word = request.POST.get('id_word')
    id_lesson = request.POST.get('id_lesson')
    lesson = get_object_or_404(Lesson, id=id_lesson)
    count_word = lesson.word.all().count()
    if count_word >= 10:
        return render(request, 'lesson/admin/admin_add_word_lesson_error.html',
                      {'error': 'Số lượng từ trong Lesson đã >=10, Không thể thêm từ vào Lesson',
                       'id_lesson': id_lesson})
    else:
        lesson.word.add(Word.objects.get(id=id_word))
        lesson.save()
        return HttpResponseRedirect(reverse('admin:admin-add-word-lesson', kwargs={'pk': id_lesson}))


@requirement_admin
def remover_word_lesson(request):
    id_word = request.POST.get('id_word')
    id_lesson = request.POST.get('id_lesson')
    lesson = get_object_or_404(Lesson, id=id_lesson)
    lesson.word.remove(Word.objects.get(id=id_word))
    lesson.save()
    return HttpResponseRedirect(reverse('admin:admin-add-word-lesson', kwargs={'pk': id_lesson}))


@requirement_admin
def admin_re_user_lesson(request):
    id_user = request.POST.get('id_user', '')
    id_lesson = request.POST.get('id_lesson', '')
    lesson_user = LessonUser.objects.get(user=User.objects.get(id=id_user), lesson=Lesson.objects.get(id=id_lesson))
    lesson_user.status = False
    lesson_user.save()
    return HttpResponseRedirect(reverse_lazy('admin:admin-detail-lesson', kwargs={'pk': id_lesson}))
