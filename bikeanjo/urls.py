# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
import front.views
admin.autodiscover()

urlpatterns = [
    # the django admin
    url(r'^admin/', include(admin.site.urls)),

    # django allauth
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/signup/', front.views.SignupView.as_view()),
    url(r'^accounts/', include('allauth.urls')),

    # bikeanjo urls
    url(r'^$', front.views.HomeView.as_view(), name='home'),
    url(r'^how-can-you-help/$', front.views.TrackView.as_view(), name='help_offer'),
    url(r'^login/', TemplateView.as_view(template_name="login.html")),
]
