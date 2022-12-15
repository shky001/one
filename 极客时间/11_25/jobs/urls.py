# from django.conf.urls import url
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

]
