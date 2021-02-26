#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.


""" 
    Context data available for all templates 
"""
from .models import Project, Profile

def project_renderer(request):
    """
    Return the project's thematic areas
    """
    return {
        'theme_list':Project.objects.order_by().values_list('thematic_area', flat=True).distinct(),
    }

def cbo_profile(request):
    """
    Deliver website data and cbo's profile information at 
    a single instance for easy rendering in all templates.
    """
    try:
        profile = Profile.objects.get()        
        contact = profile.contact_set.get()
        address = profile.address_set.get()
    except:
        print("Error fetching profile information")
        return {}
    else:
        return {
            'profile': profile,
            'contact': contact,
            'address': address
        }