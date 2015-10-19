from django.conf.urls import url

from user import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'
urlpatterns = [

    ##################################################
    ##
    ## Url user
    ##
    ##################################################
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^logout/$', views.singout, name='logout'),
    url(r'^update_profile/(?P<pk>[0-9]+)/$', views.UpadateProfile.as_view(), name='edit_profile'),
    url(r'^change_pass/$', views.changepass, name='change_pass'),





]
