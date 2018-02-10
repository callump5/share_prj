from django.conf.urls import url


import views


urlpatterns = [
    url(r'^contact-us/$', views.contact_us),
]