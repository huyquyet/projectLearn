from django.conf.urls import url

from admin.user import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    url(r'^$', views.AdminUserView.as_view(), name='admin-index-list-user'),
    url(r'^user/$', views.AdminUserView.as_view(), name='admin-index-user'),
    url(r'^manage/$', views.AdminManageView.as_view(), name='admin-index-manage'),
]
