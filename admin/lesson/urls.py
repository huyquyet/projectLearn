from django.conf.urls import url

from admin.lesson import views

__author__ = 'FRAMGIA\nguyen.huy.quyet'

urlpatterns = [
    url(r'^$', views.AdminListLessonView.as_view(), name='admin-list-lesson'),
    url(r'^create/$', views.AdminCreateLessonView.as_view(), name='admin-create-lesson'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.AdminEditLessonView.as_view(), name='admin-edit-lesson'),
    url(r'^delete/$', views.admin_delete_lesson, name='admin-delete-lesson'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.AdminDetailLessonView.as_view(), name='admin-detail-lesson'),
    url(r'^re_user/$', views.admin_re_user_lesson, name='admin-re-user-lesson'),

    url(r'^add_word/(?P<pk>[0-9]+)/$', views.AdminAddWordLessonView.as_view(), name='admin-add-word-lesson'),
    url(r'^addword/$', views.add_word_lesson, name='admin-add-word'),
    url(r'^reword/$', views.remover_word_lesson, name='admin-re-word'),
]
