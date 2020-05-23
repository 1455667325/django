from django.conf.urls import url
from datenode import views

urlpatterns = [
    url(r'^index', views.index),
    url(r'^getNode', views.getNode),
]