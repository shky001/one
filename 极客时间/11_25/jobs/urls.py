# from django.conf.urls import url
from django.conf import settings
from django.urls import path

from django.urls import re_path as url

from jobs import views

urlpatterns = [
    url(r"^joblist/",views.joblist,name = "joblist"),
    url(r"^job/(?P<job_id>\d+)/$",views.detail,name="detail"),

    # 首页自动跳转到 职位列表
    url(r"^$", views.joblist, name="name"),
    # path("", views.joblist, name="name"),

    # 提交简历
    path('resume/add/', views.ResumeCreateView.as_view(), name='resume-add'),

    path('resume/<int:pk>/', views.ResumeDetailView.as_view(), name='resume-detail'),

]


if settings.DEBUG :
    # 有 XSS 漏洞的视图页面，
    urlpatterns += [url(r'^detail_resume/(?P<resume_id>\d+)/$', views.detail_resume, name='detail_resume'),]
