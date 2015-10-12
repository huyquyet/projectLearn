from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator

from django.views.generic import ListView, CreateView, UpdateView, DetailView

from admin.forms import CreateCourseViewForm

from lesson.models import Course

__author__ = 'FRAMGIA\nguyen.huy.quyet'

requirement_admin = user_passes_test(lambda u: u.is_staff, login_url='admin:login-admin')


class AdminListCourseView(ListView):
    model = Course
    template_name = 'course/admin/admin_list_course.html'
    # context_object_name = 'list_course'
    paginate_by = 15

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminListCourseView, self).dispatch(request, *args, **kwargs)


class AdminCreateCourseView(CreateView):
    form_class = CreateCourseViewForm
    template_name = 'course/admin/admin_create_course.html'
    # fields = ['name', 'content']

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminCreateCourseView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin:admin-list-course')


class AdminEditCourseView(UpdateView):
    model = Course
    template_name = 'course/admin/admin_edit_course.html'
    # context_object_name = ''
    fields = ['name', 'content']

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminEditCourseView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin:admin-detail-course', kwargs={'pk': self.object.id})


class AdminDetailCourseView(DetailView):
    model = Course
    template_name = 'course/admin/admin_detail_course.html'
    context_object_name = 'detail_course'

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminDetailCourseView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(AdminDetailCourseView, self).get_context_data(**kwargs)
        ctx['list_lesson'] = self.object.lesson.all()
        return ctx

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.request.session['course_id'] = self.object.id
        return super(AdminDetailCourseView, self).get(request, *args, **kwargs)
