from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', BookMarkListV.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', BookMarkDetailV.as_view(), name='detail'),
]
