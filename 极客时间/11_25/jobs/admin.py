from django.contrib import admin

from jobs.models import Job
from jobs.models import Resume

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


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('username', 'applicant', 'city', 'apply_position', 'bachelor_school', 'master_school', 'major','created_date')

    readonly_fields = ('applicant', 'created_date', 'modified_date',)

    fieldsets = (
        (None, {'fields': (
            "applicant", ("username", "city", "phone"),
            ("email", "apply_position", "born_address", "gender", ), ("picture", "attachment",),
            ("bachelor_school", "master_school"), ("major", "degree"), ('created_date', 'modified_date'),
            "candidate_introduction", "work_experience","project_experience",)}),
    )

    def save_model(self, request, obj, form, change):
        obj.applicant = request.user
        super().save_model(request, obj, form, change)



# admin.site.register(Job)
admin.site.register(Job,JobAdmin)
admin.site.register(Resume, ResumeAdmin)
