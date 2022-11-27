from django.contrib import admin

from jobs.models import Job
# Register your models here.

# 定义管理类
class JobAdmin(admin.ModelAdmin):
    # 隐藏后三个字段，让系统自动生成
    exclude = ('creator','created_date','modified_date')
    # 页面列表展示的字段
    list_display = ('job_name','job_type','job_city','creator','created_date','modified_date')

    def save_model(self, request, obj, form, change):
        # 设置创建人为当前用户
        obj.creator = request.user
        # 调用父类方法保存对象
        super().save_model(request, obj, form, change)

# admin.site.register(Job)
admin.site.register(Job,JobAdmin)
