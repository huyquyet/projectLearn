from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.decorators import method_decorator

from django.views.generic import ListView, CreateView, UpdateView, DetailView

from lesson.models import Lesson, Course

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
        return reverse('admin:admin-list-lesson')


class AdminDetailLessonView(DetailView):
    model = Lesson
    template_name = 'lesson/admin/admin_detail_lesson.html'
    context_object_name = 'detail_lesson'

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminDetailLessonView, self).dispatch(request, *args, **kwargs)
