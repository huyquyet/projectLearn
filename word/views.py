# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin

from word.models import Word, Language


class UserWordIndexView(ListView):
    # model = Word
    template_name = 'word/user/word_index.html'
    # context_object_name = 'list_word'
    paginate_by = 12

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        if search == '':
            return Word.objects.all()
        else:
            return Word.objects.filter(name__icontains=search)


class UserWordView(SingleObjectMixin, ListView):
    # model = Word
    template_name = 'word/user/word_index.html'
    # context_object_name = 'list_word'
    paginate_by = 12

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Language.objects.all())
        return super(UserWordView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        if search == '':
            return self.object.word.all()
        else:
            return self.object.word.filter(name__icontains=search)


class UserDetailWordView(DetailView):
    model = Word
    template_name = 'word/user/word_detail.html'
    context_object_name = 'detail_word'

    def get_context_data(self, **kwargs):
        ctx = super(UserDetailWordView, self).get_context_data(**kwargs)
        ctx['list_lesson'] = self.object.lesson.all()
        return ctx


class UserWordMemoryView(ListView):
    # model = Word
    template_name = 'word/user/word_list_memory.html'
    paginate_by = 12

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        if search == '':
            return Word.objects.filter(user=self.request.user)
        else:
            return Word.objects.filter(user=self.request.user, name__icontains=search)
