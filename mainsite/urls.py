"""
    This module contains mainsite urls
"""
from django.urls import path
from mainsite.views import *
app_name = 'mainsite'
urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('about/team/', team, name='team'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('get_involved/partnership', partnership, name='partnership'),
    path('contact/', contact, name='contact'),
    path('contact/message/', send_message, name="message"),
    path('get_involved/careers/', careers, name='careers'),
    path('news-and-events/', NewEventView.as_view(), name='new_event'),
    path('downloads/', downloads, name='downloads'),
    path('projects-and-programmes/', projects, name='proj_and_prog'),
    path('projects-and-programmes/<str:thematic_area>/', ProjectListView.as_view(), name='projects'),
    path('projects-and-programmes/<str:thematic_area>/<int:pk>/', ProjectDetailView.as_view(), name='project_details'),
    path('get_involved/', get_involved, name='involve'),
    path('get_involved/donate', donate, name='donate')
]
