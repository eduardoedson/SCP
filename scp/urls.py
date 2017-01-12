"""scp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.generic.base import TemplateView

import servicos.urls
import usuarios.urls
from usuarios.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', TemplateView.as_view(
        template_name='index.html'), name='home'),
    url(r'^404/$', TemplateView.as_view(template_name='404.html'), name='404'),

    url(r'', include(usuarios.urls)),
    url(r'', include(servicos.urls)),

    url(r'^$', login, {
        'template_name': 'login.html',
        'authentication_form': LoginForm
        },
        name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout')
]
