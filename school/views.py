from django.shortcuts import render
from .models import SchoolPage, Gallery

def home(request):
    # Helper function to safely get pages
    def get_page(title):
        try:
            return SchoolPage.objects.get(title=title)
        except SchoolPage.DoesNotExist:
            return None
    
    # Get all pages for different sections
    pages = {
        'header_page': get_page('Header'),
        'welcome_page': get_page('Welcome'),
        'mission_page': get_page('Mission'),
        'programs_page': get_page('Programs'),
        'faculty_page': get_page('Faculty'),
        'facilities_page': get_page('Facilities'),
        'contact_page': get_page('Contact'),
    }
    
    # Get latest gallery images
    pages['gallery_images'] = Gallery.objects.all().order_by('-date_added')[:6]
    
    return render(request, 'school/home.html', pages)