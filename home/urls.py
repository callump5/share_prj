
from django.conf.urls import url, include
from django.contrib import admin

import views


urlpatterns = [

    url(r'$', views.get_home),

    url(r'googlec43a07e975a1e4ca/', views.get_an)


]