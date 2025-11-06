from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .forms import EnquiryForm
from .models import *

def site_settings(request):
    settings = SiteSettings.objects.first()
    return {'site_settings': settings}

def some_view(request):
    footer = Footer.objects.first()
    return render(request, 'footer.html', {'footer': footer})

def home(request):
    section_one = HomeSectionOne.objects.first()
    section_two = HomeSectionTwo.objects.first()
    section_two_client_boxes = section_two.boxes.all() if section_two else []
    section_three = HomeSectionThree.objects.first()
    section_three_boxes = HomeSectionThreeBox.objects.all()
    section_four = HomeSectionFour.objects.first()
    section_four_boxes = HomeSectionFourServiceBox.objects.all()
    section_five = HomeSectionFive.objects.first()
    section_five_reviews = HomeSectionFiveReviewCard.objects.all()
    section_six = HomeSectionSix.objects.first()
    section_six_tabs = HomeSectionSixTab.objects.prefetch_related('images').all()
    section_seven = HomeSectionSeven.objects.first()
    section_seven_boxes = section_seven.boxes.all() if section_seven else []
    context = {
       'section_one': section_one,
       'section_two': section_two,
       'section_two_client_boxes': section_two_client_boxes,
       'section_three': section_three,
       'section_three_boxes': section_three_boxes,
       'section_four': section_four,
       'section_four_boxes': section_four_boxes,
       'section_five': section_five,
       'section_five_reviews': section_five_reviews,
       'section_six': section_six,
       'section_six_tabs': section_six_tabs,
       "section_seven": section_seven,
       "section_seven_boxes": section_seven_boxes,
    }
    return render(request, 'home.html', context)

def submit_enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save()

            # email to admin
            subject_admin = f"New Enquiry: {enquiry.service}"
            message_admin = f"""
Name: {enquiry.name}
Email: {enquiry.email}
Phone: {enquiry.phone}
Service: {enquiry.service}
Message:
{enquiry.message}
"""
            admin_email = settings.EMAIL_HOST_USER
            try:
                send_mail(subject_admin, message_admin, settings.DEFAULT_FROM_EMAIL, [admin_email], fail_silently=False)
            except Exception as e:
                # you can log here
                print("Admin email send error:", e)

            # confirmation email to user (HTML)
            subject_user = "Thank you for your enquiry"
            html_content = render_to_string('emails/enquiry_confirmation.html', {'enquiry': enquiry})
            try:
                msg = EmailMultiAlternatives(subject_user, message_admin, settings.DEFAULT_FROM_EMAIL, [enquiry.email])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
            except Exception as e:
                print("User email send error:", e)

            # redirect to thank you page
            return redirect('enquiry_thanks')
        else:
            # Form invalid -> you can return to same page with errors; for modal you might need AJAX
            messages.error(request, "Please complete the form correctly.")
            return redirect('home')  # or wherever you prefer
    # not POST
    return redirect('home')

def about_us(request):
    about = AboutContent.objects.first()         # instead of filter(is_active=True).first()
    features = AboutFeature.objects.all()       # instead of filter(is_active=True)
    return render(request, 'about_us.html', {"about": about, "features": features})


def design_services(request):
    section_one = DesignServiceSectionOne.objects.first()
    section_two = DesignServiceSectionTwo.objects.all()
    
    section_three = DesignServiceSectionThree.objects.first()
    section_three_boxes = DesignServiceSectionThreeBox.objects.filter(section=section_three)

    context = {
        'section_one': section_one,
        'section_two': section_two,
        'section_three': section_three,
        'section_three_boxes': section_three_boxes,
    }
    return render(request, 'design_services.html', context)


def website_development(request):
    section_one = WebsiteDevelopmentSectionOne.objects.first()
    section_two = WebsiteDevelopmentSectionTwo.objects.all()
    section_three = WebsiteDevelopmentSectionThree.objects.first()
    section_three_boxes = section_three.boxes.all() if section_three else []
    section_four = WebsiteDevelopmentSectionFour.objects.first()
    section_four_boxes = WebsiteDevelopmentSectionFourBox.objects.filter(section=section_four)
    context = {
        'section_one': section_one,
        'section_two': section_two,
        'section_three' : section_three,
        'section_three_boxes': section_three_boxes,
        'section_four': section_four,
        'section_four_boxes': section_four_boxes,
    }
    return render(request, 'website_development.html', context)

def software_development(request):
    section_one = SoftwareDevelopmentSectionOne.objects.first()
    section_two = SoftwareDevelopmentSectionTwo.objects.all()
    section_three = SoftwareDevelopmentSectionThree.objects.first()
    section_three_boxes = SoftwareDevelopmentSectionThreeBox.objects.filter(section=section_three)
    context = {
        "section_one": section_one,
        "section_two": section_two,
        "section_three": section_three,
        "section_three_boxes": section_three_boxes,
    }
    return render(request, 'software_development.html', context)
