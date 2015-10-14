from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.generic import ListView

__author__ = 'FRAMGIA\nguyen.huy.quyet'
requirement_admin = user_passes_test(lambda u: u.is_staff, login_url='admin:login-admin')


class AdminManageView(ListView):
    model = User
    template_name = 'user/admin/admin_profile_user.html'
    # context_object_name = 'list_user_profile'

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminManageView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(is_staff=True)

    def get_context_data(self, **kwargs):
        # search = ''
        search = self.request.GET.get('search', '')
        context = super(AdminManageView, self).get_context_data(**kwargs)
        if search != '':
            context['list_user_profile'] = self.model.objects.filter(is_staff=True, username=search)
        else:
            context['list_user_profile'] = self.model.objects.filter(is_staff=True)
        context['staff'] = True
        return context


class AdminUserView(ListView):
    model = User
    template_name = 'user/admin/admin_profile_user.html'
    # context_object_name = 'list_user_profile'

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminUserView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(is_staff=False)

    def get_context_data(self, **kwargs):
        # search = ''
        search = self.request.GET.get('search', '')
        context = super(AdminUserView, self).get_context_data(**kwargs)
        if search != '':
            context['list_user_profile'] = self.model.objects.filter(is_staff=False, username=search)
        else:
            context['list_user_profile'] = self.model.objects.filter(is_staff=False)
        context['staff'] = False
        return context
