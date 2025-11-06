from django.urls import path
from . import views
from .views import submit_enquiry
from django.views.generic import TemplateView
from .models import *

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('design-services/', views.design_services, name='design_services'),
    path('website-development/', views.website_development, name='website_development'),
    path('software-development/', views.software_development, name='software_development'),
    path('submit-enquiry/', submit_enquiry, name='submit_enquiry'),
    path('enquiry-thanks/', TemplateView.as_view(template_name="enquiry_thanks.html"), name='enquiry_thanks'),
]