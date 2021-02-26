

from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import MessageForm
from django.contrib import messages
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.


from django.views.generic import ListView, DetailView
from django.utils import timezone
# Create your views here.


def about(request):
    """About us page view"""
    
    return render(request, 'mainsite/about.html')

def careers(request):
    """Careers page view"""
    return render(request, 'mainsite/careers.html')

def contact(request):
    """Contact us page view"""
    form = MessageForm
   
    context = {
        'form': form,
        
    }
    return render(request, 'mainsite/contact.html', context)

def donate(request):
    return render(request, 'mainsite/donate.html')

def downloads(request):
    """
    Downloads view
    """
    return render(request, 'mainsite/downloads.html')

class GalleryView(ListView):
    """
    View for cbo's pictures
    """
    model = Media
    context_object_name = "media_list"
    template_name = "mainsite/gallery.html"

    def get_queryset(self):
        return Media.objects.filter(carousel=False).order_by('id')[::-1]
    


def get_involved(request):
    return render(request, 'mainsite/involve.html')

def index(request):
    """Home page view"""
    carousel = Media.objects.filter(carousel=True)[:5]
    return render(request, 'mainsite/home.html', {'carousel': carousel})

def director_message(request):
    """ Render the Message from director."""
    return render(request, 'mainsite/director_msg.html')

class NewEventView(ListView):
    """
    View for news and events.
    """
    model = NewsEvent
    context_object_name = "item_list"
    template_name = 'mainsite/news-events.html'

    def get_queryset(self):
        return NewsEvent.objects.filter(
            pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    


def team(request):
    """Team page view"""
    return render(request, 'mainsite/team.html')
    
#Projects and programmes view
def projects(request):
    projects = Project.objects.all()
    return render(request, 'mainsite/projects_home.html', {'projects': projects})


class ProjectListView(ListView):
    '''
    Lists projects gouped by thematic area
    '''
    model = Project
    paginate_by = 8

    def get_queryset(self):
        return Project.objects.filter(thematic_area=self.kwargs['thematic_area'])

class ProjectDetailView(DetailView):
    '''
    View of a single project
    '''
    model = Project


    def get_queryset(self):
        """
        Return the project according to its thematic area
        """
        return Project.objects.filter(thematic_area=self.kwargs['thematic_area']).order_by('-start_date')

    
def partnership(request):
    """
    View for partnership
    """
    donations = Donation.objects.all()
    partners = Partner.objects.all()
    context = {
        'donations': donations,
        'partners': partners,
    }
    return render(request, 'mainsite/partner.html', context)

def send_message(request):
    
    if request.method == 'POST':
        form = MessageForm(request.POST or None)
        try:
            if form.is_valid:
                form.save()
                messages.success(request, 'Your message has been received, we will get back to you as soon as possible')
                return HttpResponseRedirect(reverse('mainsite:contact', ))
        except:
            return render(request, 'mainsite/contact.html',
                {
                    'form':form,
                    'error_message': 'OOPS!, You may have entered incorrect data in one of the fields'
                    }
                )

    else:
        form = MessageForm()


def volunteer(request):
    """
    Render volunteer page
    """
    return render(request, 'mainsite/volunteer.html',)
