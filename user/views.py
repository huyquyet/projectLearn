# Create your views here.
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import FormView, ListView, CreateView, UpdateView, DetailView

from lesson.models import Course



def index(request):
    return HttpResponseRedirect(reverse('lesson:course-index'))


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'

    def get_success_url(self):
        link = self.request.POST.get('next', False)
        if link:
            return link
        else:
            return reverse('fels:index')

    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # if self.request == 'POST':
        user_form = form.get_user()
        login(self.request, user_form)
        return super(LoginView, self).form_valid(form)


@login_required()
def singout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('fels:index'))


class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'user/register.html'

    def dispatch(self, request, *args, **kwargs):
        return super(Register, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # if self.request == 'POST':
        #     if form.is_valid():
        form.instance.is_staff = False
        form.save()
        return super(Register, self).form_valid(form)

    def get_success_url(self):
        return reverse('fels:login')


class UpadateProfile(UpdateView):
    model = User
    template_name = 'user/editprofile.html'
    fields = ['first_name', 'last_name', 'email']

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object != request.user:
            raise PermissionDenied
        return super(UpadateProfile, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('fels:index')


#
# class ChangpassView(ListView):
#     model = User
#     template_name = 'user/change_pass.html'
#     form_class = PasswordChangeForm
#
#     @login_required()
#     def dispatch(self, request, *args, **kwargs):
#         return super(ChangpassView, self).dispatch(request, *args, **kwargs)
#
#     def get_success_url(self):
#         return reverse('fels:index')


def changepass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('fels:index'))
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'user/change_pass.html', {'form': form})


