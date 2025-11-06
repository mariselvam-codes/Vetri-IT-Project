from .models import *

def site_settings(request):
    settings = SiteSettings.objects.first()
    return {'site_settings': settings}

def navbar_logo(request):
    footer = Footer.objects.filter(is_active=True).first()
    return {
        "logo": logo.objects.first(),
        "footer": footer,
        "footer_video": footer  # pass same object
    }
