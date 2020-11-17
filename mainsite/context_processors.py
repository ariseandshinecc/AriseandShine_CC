# Context data available for all templates
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