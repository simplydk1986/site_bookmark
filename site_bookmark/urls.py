from django.conf.urls import url
from django.contrib import admin
from bookmark.models import BookMark
from django.views.generic import ListView, DetailView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bookmark/$', ListView.as_view(model=BookMark), name='index'),
    url(r'^bookmark/(?P<pk>\d+)/$', DetailView.as_view(model=BookMark), name='detail'),
]
