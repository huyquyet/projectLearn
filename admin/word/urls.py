from django.conf.urls import url

from admin.word import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    url(r'^$',views.AdminWordIndexView.as_view(), name='admin-index-word'),
]