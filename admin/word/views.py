from django.views.generic import ListView, CreateView
from django.views.generic.detail import SingleObjectMixin

from word.models import Word

__author__ = 'FRAMGIA\nguyen.huy.quyet'


class AdminWordIndexView(SingleObjectMixin,  ListView):
    model = Word
    template_name = 'word/admin/admin_list_word.html'
    context_object_name = 'list_word'
    paginate_by = 20

# class cre(CreateView ):

