"""Test_Django01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from django.conf.urls import url,include
from django.conf.urls import include
from django.urls import re_path as url
from django.utils.translation import gettext as _

from . import views
# from Test_Django01 import views
from jobs.models import Job

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'jobs', JobViewSet)


urlpatterns = [
    url(r"^",include("jobs.urls")),
    path('grappelli/', include('grappelli.urls')),
    # path(r'', admin.site.urls),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),

    url(r'^accounts/', include('registration.backends.simple.urls')),

    path('i18n/', include('django.conf.urls.i18n')),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

    # 使用 login_with_captcha 作为管理员的登陆页
    url(r'^admin/login/?$', views.login_with_captcha, name='adminlogin'),

    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),

    path('captcha/', include('captcha.urls')),

    path("clogin/", views.login_with_captcha, name="clogin"),

]


from django.conf.urls import include
from django.conf import settings

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


admin.site.site_header = _('匠果科技招聘管理系统')


