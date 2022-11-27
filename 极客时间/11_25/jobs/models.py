from django.db import models
# 导入系统自带的对象
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

JobType = [(0,"技术类"),
           (1,"运营类"),
           (2,"设计类")
           ]
cities = [(0,"北京市"),
          (1,"上海市"),
          (2,"天津市")
          ]

class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False,choices=JobType,verbose_name="职位类别")
    job_name = models.CharField(max_length=250,blank=False,verbose_name="职位名称")
    job_city = models.SmallIntegerField(blank=False,choices=cities,verbose_name="工作城市")
    job_responsibility = models.TextField(max_length=1024,blank=False,verbose_name="岗位职责")
    job_requirement = models.TextField(max_length=1024,blank=False,verbose_name="岗位要求")
    creator = models.ForeignKey(User,null=True,on_delete=models.SET_NULL,verbose_name="创建者")
    created_date = models.DateTimeField(verbose_name="创建日期",default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="修改日期",default=datetime.now)
