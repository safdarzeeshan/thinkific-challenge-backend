"""thinkific_api URL Configuration

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
from user_api.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('rest_auth.urls')),
    url(r'^api/registration/', include('rest_auth.registration.urls')),
    url(r'^api/currentint/', Integer.as_view(), name="current_integer"),
    url(r'^api/nextint/', NextInteger.as_view(), name="next_integer"),
]
