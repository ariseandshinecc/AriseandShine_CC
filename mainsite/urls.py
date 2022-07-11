#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.


"""
    This module contains mainsite urls
"""
from django.urls import path
from mainsite.views import *
from django.views.generic.base import TemplateView

app_name = 'mainsite'
urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('about/team/', team, name='team'),
    path('contact/', contact, name='contact'),
    path('downloads/', downloads, name='downloads'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('get_involved/', get_involved, name='involve'),
    path('get_involved/careers/', careers, name='careers'),
    path('get_involved/donate', donate, name='donate'),
    path('get_involved/partnership', partnership, name='partnership'),
    path('get_involved/volunteer', volunteer, name='volunteer'),
    path('message-from-director/', director_message, name='director_message'),
    path('news-and-events/', NewEventView.as_view(), name='new_event'),
    path('projects-and-programmes/', projects, name='proj_and_prog'),
    path('projects-and-programmes/<str:thematic_area>/', ProjectListView.as_view(), name='projects'),
    path('projects-and-programmes/<str:thematic_area>/<slug:slug>/', ProjectDetailView.as_view(), name='project_details'),
    path('robots.txt', TemplateView.as_view(template_name='mainsite/robots.txt', content_type='text/plain'),),
]