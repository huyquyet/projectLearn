# Create your views here.
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from lesson.models import Course, Lesson, LessonUser

requirement_admin = user_passes_test(lambda u: u.is_staff, login_url='fels:login-admin')


# Course
@requirement_admin
def admin_delete_course(request):
    pass


class UserCourseIndexView(ListView):
    model = Course
    template_name = 'course/user/course_index.html'
    # context_object_name = 'list_course'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        ctx = super(UserCourseIndexView, self).get_context_data(**kwargs)

        return ctx

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        if search == '':
            return Course.objects.filter()
        else:
            return Course.objects.filter(name__contains=search)


class UserCourseDetailView(DetailView):
    model = Course
    template_name = 'course/user/course_detail.html'
    context_object_name = 'detail_course'

    def get_context_data(self, **kwargs):
        ctx = super(UserCourseDetailView, self).get_context_data(**kwargs)
        list_lesson = self.object.lesson.filter(status=True)
        for i in list_lesson:
            if LessonUser.objects.filter(lesson=i, user=self.request.user).exists():
                i.status = True
            else:
                i.status = False
        ctx['list_lesson'] = list_lesson
        return ctx


class UserLessonIndexView(ListView):
    model = Lesson
    template_name = 'lesson/user/lesson_index.html'
    # context_object_name = ''
    paginate_by = 12

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        if search == '':
            return Lesson.objects.filter(status=True)
        else:
            return Lesson.objects.filter(status=True, name__contains=search)


class UserLessonDetailView(DetailView):
    model = Lesson
    template_name = 'lesson/user/lesson_detail.html'
    context_object_name = 'detail_lesson'

    def get_queryset(self):
        return Lesson.objects.filter(status=True)

    def get_context_data(self, **kwargs):
        ctx = super(UserLessonDetailView, self).get_context_data(**kwargs)
        ctx['words'] = self.object.word.all()
        ctx['course'] = self.object.course.name
        users = LessonUser.objects.filter(lesson=self.object)
        ctx['users'] = [User.objects.get(id=i.user.id) for i in users]
        if LessonUser.objects.filter(lesson=self.object, user=self.request.user).exists():
            if LessonUser.objects.get(lesson=self.object, user=self.request.user).status:
                ctx['join'] = True
            else:
                ctx['join'] = False
        else:
            ctx['join'] = False
        return ctx


def user_lesson_join(request):
    id_lesson = request.POST.get('id_lesson')
    id_user = request.POST.get('id_user')
    if id_lesson == '' or id_user == '':
        return render(request, 'lesson/user/lesson_user_join_error.html')
    else:
        lesson = get_object_or_404(Lesson, id=id_lesson)
        user = get_object_or_404(User, id=id_user)
        lesson_user, create = LessonUser.objects.get_or_create(user=user, lesson=lesson)
        lesson_user.status = True
        lesson_user.save()
        return HttpResponseRedirect(reverse('lesson:lesson-detail', kwargs={'pk': id_lesson}))


