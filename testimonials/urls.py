from django.conf.urls import url


import views


urlpatterns = [

    url(r'^testimonials/$', views.get_testimonials),


]