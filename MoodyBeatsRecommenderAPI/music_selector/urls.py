"""music_selector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view 
from rest_framework_swagger.views import get_swagger_view

from .views import home

API_TITLE = 'MoodyBeats-Recommender API'

API_DESCRIPTION = 'A Web API for generating song recommendations based on User similarity'

schema_view_swagger = get_swagger_view(title=API_TITLE)
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^songs/', include('songs.urls', namespace='song')),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    url(r'^schema/', schema_view),
    url(r'^swagger-docs/', schema_view_swagger),
]





