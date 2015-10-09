from django.conf.urls import url, include

from admin import views
# from admin.course import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    ##################################################
    ##
    ## Url Admin
    ##
    ##################################################
    url(r'^$', views.adminindex, name='index-admin'),
    url(r'^login/$', views.AdminLoginView.as_view(), name='login-admin'),
    url(r'^logout/$', views.logout_admin, name='logout-admin'),
    url(r'^profile/(?P<pk>[0-9]+)/$', views.AdminProfileView.as_view(), name='admin-profile'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.AdminEditProfileView.as_view(), name='admin-edit-profile'),

    #################################################
    ##
    ##  Course
    ##
    #################################################
    url(r'^course/', include('admin.course.urls')),

    #################################################
    ##
    ##  Lesson
    ##
    #################################################
    url(r'^lesson/', include('admin.lesson.urls')),

    #################################################
    ##
    ##  Word
    ##
    #################################################
    url(r'^word/', include('admin.word.urls')),
]
