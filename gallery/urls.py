from django.conf.urls import url


import views


urlpatterns = [
    url(r'^staff/$', views.get_staff),
    url(r'^students/gallery$', views.get_students),
]