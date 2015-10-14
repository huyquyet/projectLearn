from django.conf.urls import url

from admin.course import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    url(r'^$', views.AdminListCourseView.as_view(), name='admin-list-course'),
    url(r'^(?P<pk>[0-9]+)/$', views.AdminCourseView.as_view(), name='admin-course'),
    url(r'^delete/$', views.AdminListCourseView.as_view(), name='admin-delete-course'),
    url(r'^create/$', views.AdminCreateCourseView.as_view(), name='admin-create-course'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.AdminEditCourseView.as_view(), name='admin-edit-course'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.AdminDetailCourseView.as_view(), name='admin-detail-course'),
]
