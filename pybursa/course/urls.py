from django.conf.urls import url
from . import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'^$', views.course_),
    url(r'^course/(?P<identer>\d+)$', views.course_description),
    # url(r'^students/', views.students),
    url(r'^students/$', views.StudentListView.as_view(), name='list'),
    url(r'^student/(?P<pk>\d+)$', views.StudentDetailView.as_view()),
    url(r'^course/edit/(?P<pk>\d+)$', views.course_edit),
    url(r'^course/add$', views.course_add),
    url(r'^course/remove/(?P<pk>\d+)$', views.course_delete),
    url(r'^lesson/add/(?P<pk>\d+)$', views.lesson_add),
    url(r'^students/add$', views.StudentCreateView.as_view()),
    url(r'^students/remove/(?P<pk>\d+)$', views.StudentDeleteView.as_view()),
    url(r'^students/edit/(?P<pk>\d+)$', views.StudentUpdateView.as_view()),

]
