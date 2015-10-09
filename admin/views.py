from django.contrib import auth
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login
from django.utils.decorators import method_decorator
from django.views.generic import FormView, DetailView, UpdateView, ListView
# Create your views here.


requirement_admin = user_passes_test(lambda u: u.is_staff, login_url='admin:login-admin')


def adminindex(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return render(request, 'admin/index.html')
        else:
            return HttpResponseRedirect(reverse('admin:login-admin'))
    else:
        return HttpResponseRedirect(reverse('admin:login-admin'))


class AdminLoginView(FormView):
    form_class = AdminAuthenticationForm
    template_name = 'admin/login.html'

    def get_success_url(self):
        link = self.request.POST.get('next', False)
        if link:
            return link
        else:
            return reverse('admin:index-admin')

    def dispatch(self, request, *args, **kwargs):
        return super(AdminLoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user_form = form.get_user()
        login(self.request, user_form)
        return super(AdminLoginView, self).form_valid(form)


# @method_decorator(requirement_admin)
def logout_admin(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('admin:index-admin'))


class AdminProfileView(DetailView):
    model = User
    template_name = 'admin/detail_profile.html'
    context_object_name = ''

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminProfileView, self).dispatch(request, *args, **kwargs)


class AdminEditProfileView(UpdateView):
    model = User
    template_name = 'admin/edit_profile.html'
    # context_object_name = ''
    fields = ['first_name', 'last_name', 'email']

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminEditProfileView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('admin:admin-profile', kwargs={'pk': self.request.user.id})


