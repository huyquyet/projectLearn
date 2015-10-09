from django.conf.urls import url

from admin.lesson import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    url(r'^$', views.AdminListLessonView.as_view(), name='admin-list-lesson'),
    url(r'^create/$', views.AdminCreateLessonView.as_view(), name='admin-create-lesson'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.AdminEditLessonView.as_view(), name='admin-edit-lesson'),
    url(r'^delete/$', views.AdminListLessonView.as_view(), name='admin-delete-lesson'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.AdminDetailLessonView.as_view(), name='admin-detail-lesson'),
]
