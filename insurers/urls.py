from django.conf.urls import url
from insurers import views

urlpatterns = [
    url(r'^risks/$', views.risk_list),
    url(r'^risks/(?P<id>[0-9]+)/$', views.risk_detail),
    ]
