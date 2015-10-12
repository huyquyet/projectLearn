from django.contrib.auth.decorators import user_passes_test
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator

from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.views.generic.detail import SingleObjectMixin
# from admin.forms import CreateQuestionWordView

from word.models import Word, Language, Question

__author__ = 'FRAMGIA\nguyen.huy.quyet'
requirement_admin = user_passes_test(lambda u: u.is_staff, login_url='admin:login-admin')


class AdminWordIndexView(ListView):
    model = Word
    template_name = 'word/admin/admin_list_word.html'
    # context_object_name = 'list_word'
    paginate_by = 15

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminWordIndexView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(AdminWordIndexView, self).get_context_data(**kwargs)
        return ctx


class AdminWordView(SingleObjectMixin, ListView):
    template_name = 'word/admin/admin_word.html'
    paginate_by = 15

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminWordView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Language.objects.all())
        return super(AdminWordView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(AdminWordView, self).get_context_data(**kwargs)
        ctx['lang'] = Language.objects.all()
        return ctx

    def get_queryset(self):
        return self.object.word.all()


class AdminCreateWordView(CreateView):
    model = Word
    template_name = 'word/admin/admin_create_word.html'
    # context_object_name = ''
    fields = ['name', 'meaning']
    # form_class = CreateWordViewForm

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminCreateWordView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if self.request.POST.get('lang_id'):
            form.instance.language = Language.objects.get(id=self.request.POST.get('lang_id'))
        else:
            form.instance.language = Language.objects.get(id=1)
        form.save()
        return super(AdminCreateWordView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(AdminCreateWordView, self).get_context_data(**kwargs)
        ctx['list_lang'] = Language.objects.all()
        return ctx

    def get_success_url(self):
        return reverse('admin:admin-index-word')


class AdminEditWordView(UpdateView):
    model = Word
    template_name = 'word/admin/admin_edit_word.html'
    context_object_name = ''
    fields = ['name', 'meaning']
    # form_class = CreateWordViewForm

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminEditWordView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(AdminEditWordView, self).get_context_data(**kwargs)
        ctx['list_lang'] = Language.objects.all()
        ctx['lang_word'] = self.object.language.id
        return ctx

    def get_success_url(self):
        return reverse('admin:admin-index-word')


class AdminDetailWordView(DetailView):
    model = Word
    template_name = 'word/admin/admin_detail_word.html'
    context_object_name = 'detail_word'

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminDetailWordView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(AdminDetailWordView, self).get_context_data(**kwargs)
        ctx['question'] = self.object.question.all()
        num = self.object.question.all().count()
        if num < 3:
            ctx['num'] = num
        else:
            ctx['num'] = []
        return ctx


class AdminCreateQuestionWordView(CreateView):
    model = Question
    template_name = 'word/admin/admin_create_question_word.html'
    fields = ['answer', 'check']
    # form_class = CreateQuestionWordView

    @method_decorator(requirement_admin)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminCreateQuestionWordView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(AdminCreateQuestionWordView, self).get_context_data(**kwargs)
        ctx['detail_word'] = Word.objects.get(id=self.kwargs['pk'])
        id_word = self.kwargs['pk']
        num = Question.objects.filter(word__id=id_word).count()
        if num >= 3:
            ctx['number'] = num
        else:
            ctx['number'] = []
        return ctx

    def form_valid(self, form):
        id_word = self.kwargs['pk']
        num = Question.objects.filter(word__id=id_word).count()
        if num >= 3:
            return render(self.request, 'word/admin/admin_create_question_word_error.html',
                          {'error': 'Loi tạo hown3 câu trả lời.', 'id': id_word})
        else:
            form.instance.word = Word.objects.get(id=id_word)
            form.save()
            return super(AdminCreateQuestionWordView, self).form_valid(form)

    def get_success_url(self):
        return reverse('admin:admin-detail-word', kwargs={'pk': self.kwargs['pk']})


@requirement_admin
def detele_question(request):
    id_word = request.POST.get('id_word')
    id_question = request.POST.get('id_question')
    check = get_object_or_404(Question, id=id_question)
    if check:
        check.delete()
    return HttpResponseRedirect(reverse('admin:admin-detail-word', kwargs={'pk': id_word}))
