from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.views.generic.detail import SingleObjectMixin

from admin.forms import CreateCourseViewForm
from lesson.models import Course
from word.models import Language

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


class AdminCourseView(SingleObjectMixin, ListView):
    template_name = 'course/admin/admin_course.html'
    paginate_by = 15

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminCourseView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Language.objects.all())
        return super(AdminCourseView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(AdminCourseView, self).get_context_data(**kwargs)
        ctx['lang'] = Language.objects.all()
        return ctx

    def get_queryset(self):
        return self.object.course.all()


class AdminCreateCourseView(CreateView):
    form_class = CreateCourseViewForm
    template_name = 'course/admin/admin_create_course.html'
    # fields = ['name', 'content']

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminCreateCourseView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin:admin-list-course')

    def get_context_data(self, **kwargs):
        ctx = super(AdminCreateCourseView, self).get_context_data(**kwargs)
        ctx['list_lang'] = Language.objects.all()
        return ctx

    def form_valid(self, form):
        if self.request.POST.get('lang_id'):
            form.instance.language = Language.objects.get(id=self.request.POST.get('lang_id'))
        else:
            form.instance.language = Language.objects.get(id=1)
        form.save()
        return super(AdminCreateCourseView, self).form_valid(form)


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

    def get_context_data(self, **kwargs):
        ctx = super(AdminEditCourseView, self).get_context_data(**kwargs)
        ctx['list_lang'] = Language.objects.all()
        return ctx

    def form_valid(self, form):
        if self.request.POST.get('lang_id'):
            form.instance.language = Language.objects.get(id=self.request.POST.get('lang_id'))
        else:
            form.instance.language = Language.objects.get(id=1)
        form.save()
        return super(AdminEditCourseView, self).form_valid(form)

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
