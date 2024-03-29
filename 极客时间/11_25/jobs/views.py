from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.views.generic.detail import DetailView

from jobs.models import Job
from jobs.models import Cities, JobTypes
from django.contrib.auth.mixins import LoginRequiredMixin
from jobs.models import Job, Resume
from django.views.generic.edit import CreateView
import html
import logging

logger = logging.getLogger(__name__)


def joblist(request):
    job_list = Job.objects.order_by('job_type')
    templates = loader.get_template('joblist.html')
    context =  {'job_list': job_list}

    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        job.type_name = JobTypes[job.job_type][1]
    # return HttpResponse(templates.render(context))
    return render(request,'joblist.html',context)

def detail(request,job_id):
    try:
        job = Job.objects.get(pk = job_id)
        job.city_name = Cities[job.job_city][1]
        logger.info('job retrieved from db :%s' % job_id)

    except Job.DoesNotExist:
        raise Http404("Job does not exist.")
    return render(request,'job.html',{'job':job})

class ResumeCreateView(LoginRequiredMixin, CreateView):
    """    简历职位页面  """
    template_name = 'resume_form.html'
    success_url = '/joblist/'
    model = Resume
    fields = ["username", "city", "phone",
        "email", "apply_position", "gender",
        "bachelor_school", "master_school", "major", "degree", "picture", "attachment",
        "candidate_introduction", "work_experience", "project_experience"]

    ### 从 URL 请求参数带入默认值
    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

'''
    直接返回  HTML 内容的视图 （这段代码返回的页面有 XSS 漏洞，能够被攻击者利用）
'''
def detail_resume(request, resume_id):
    try:
        resume = Resume.objects.get(pk=resume_id)
        content = "name: %s <br>  introduction: %s <br>" % (resume.username, resume.candidate_introduction)
        return HttpResponse(html.escape(content))
    except Resume.DoesNotExist:
        raise Http404("resume does not exist")


class ResumeDetailView(DetailView):
    """   简历详情页    """
    model = Resume
    template_name = 'resume_detail.html'
