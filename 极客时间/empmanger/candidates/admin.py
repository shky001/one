from django.contrib import admin

# Register your models here.

from .models import JobsJob, JobsResume, Candidate


admin.site.register(JobsResume)
admin.site.register(JobsJob)
admin.site.register(Candidate)
