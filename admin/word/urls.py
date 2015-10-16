from django.conf.urls import url

from admin.word import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [

    ##################################
    ## Word
    url(r'^$',views.AdminWordIndexView.as_view(), name='admin-index-word'),
    url(r'^(?P<pk>[0-9]+)/$', views.AdminWordView.as_view(), name='admin-word'),
    url(r'^create/$', views.AdminCreateWordView.as_view(), name='admin-create-word'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.AdminEditWordView.as_view(), name='admin-edit-word'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.AdminDetailWordView.as_view(), name='admin-detail-word'),
    url(r'^delete/$', views.admin_delete_word, name='admin-delete-word'),

    ################################
    ## Question

    url(r'^create/question/(?P<pk>[0-9]+)/$', views.AdminCreateQuestionWordView.as_view(),
        name='admin-create-question-word'),
    url(r'^delete/question/$', views.detele_question, name='admin-delete-question'),

]