from django.conf.urls import url

from word import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    url(r'^$', views.UserWordIndexView.as_view(), name='word-index'),
    url(r'^word_language/(?P<pk>[0-9]+)/$', views.UserWordView.as_view(), name='word-language'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.UserDetailWordView.as_view(), name='word-detail'),
]
