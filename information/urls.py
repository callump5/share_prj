from django.conf.urls import url


import views


urlpatterns = [
    url(r'^info/$', views.get_info),
]