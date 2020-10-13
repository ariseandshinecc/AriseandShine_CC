# Context data available for all templates
from .models import Project, Contact

def project_renderer(request):
    """
    Return the project's thematic areas
    """
    return {
        'theme_list':Project.objects.order_by().values_list('thematic_area', flat=True).distinct(),
    }

def contacts(request):
    """
    Returns contact objects
    """
    try:
    	contact = Contact.objects.get(pk=1)
    except:
    	print("No contact information added")
    	return {}
    else:
    	return {
    		'contact': contact,
    	}
