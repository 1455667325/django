from django.conf.urls import url
from person import views
urlpatterns = [
    url(r'^index', views.index)
]