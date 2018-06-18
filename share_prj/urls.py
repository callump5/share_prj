"""share_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

import new_settings.base

from home import views as home_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Tinymce
    url(r'', include('tinymce.urls')),

    # Home
    url(r'^$', home_view.get_home),

    # Testimonials
    url(r'', include('testimonials.urls')),

    # Staff Details
    url(r'', include('gallery.urls')),

    # Infomation

    url(r'', include('information.urls')),

    # Contact Us
    url(r'', include('contact_us.urls')),

    # Cokkies
    url(r'', include('cookies.urls')),

    # Static
    url(r'^static/(?P<path>.*)$', serve, {'document_root': new_settings.base.STATIC_ROOT}),

    # Media Root
    url(r'^media/(?P<path>.*)$', serve, {'document_root': new_settings.base.MEDIA_ROOT}),

]
