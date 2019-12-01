"""event_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('event/', include('event.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include # url
from event.views import (
    event_post_create_view,
)

admin.site.site_header = 'Event Management Administration'
admin.site.site_title = 'Event Posts Administration'
admin.site.index_title = 'Event Administration'

from searches.views import search_view
from .views import (
    home_page,
    about_page,
    contact_page,
)

urlpatterns = [
    path('', home_page),
    path('event-new/', event_post_create_view),
    path('event/', include('event.urls')),
    path('search/', search_view),
    # re_path(r'^event/(?P<slug>\w+)/$', event_post_detail_view),
    path('page/', about_page),
    path('pages/', about_page),
    re_path(r'^pages?/$', about_page),
    re_path(r'^about/$', about_page),
    path('contact/', contact_page),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
