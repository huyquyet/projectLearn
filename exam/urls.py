from django.conf.urls import url

from exam import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    url(r'^lesson/(?P<pk>[0-9]+)/$', views.UserLessonExamView.as_view(), name='exam-lesson'),
    url(r'^history/$', views.UserListHistoryExamView.as_view(), name='exam-list-history'),
    url(r'^history/detail/(?P<pk>[0-9]+)/$', views.UserHistoryExamView.as_view(), name='exam-history-detail'),
    # url(r'^lesson-exam/$', views.UserLessonExamView_1(), name='exam-lesson-1'),
]
