from django.conf.urls import url


import views


urlpatterns = [
    url(r'^staff/$', views.get_staff),
    url(r'^student/gallery/$', views.get_students),
]