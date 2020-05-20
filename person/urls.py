from django.conf.urls import url
from person import views
print(views)
urlpatterns = [
    url(r'^index', views.index)
]