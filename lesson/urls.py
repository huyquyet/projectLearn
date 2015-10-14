from django.conf.urls import url

from lesson import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    url(r'^course/$', views.UserCourseIndexView.as_view(), name='course-index'),
    url(r'^course/(?P<pk>[0-9]+)/$', views.UserCourseDetailView.as_view(), name='course-detail'),

    url(r'^$', views.UserLessonIndexView.as_view(), name='lesson-index'),
    url(r'^(?P<pk>[0-9]+)/$', views.UserLessonDetailView.as_view(), name='lesson-detail'),
    url(r'^user_join/$', views.user_lesson_join, name='lesson-user-join'),

]
