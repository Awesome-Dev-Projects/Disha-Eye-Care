from django.shortcuts import render

from doctor.models import Doctor
from .models import Speciality

# Create your views here.

def home_view(request):
    template_page='clinic/index.html'
    doctors=Doctor.objects.all()[:3]
    specialities=Speciality.objects.all()[:3]
    print(doctors)
    template_context={
        'doctors':doctors,
        'specialities':specialities
    }
    return render(request,template_page,context=template_context) 

def contact_us_view(request):
    template_page='clinic/contact_us.html'
    return render(request,template_page)

def about_us_view(request):
    template_page='clinic/about_us.html'
    return render(request,template_page)

def our_doctors_view(request):
    template_page='clinic/our_doctors.html'
    doctors=Doctor.objects.all()
    template_context={
        'doctors':doctors
    }
    return render(request,template_page,context=template_context)

def our_specialities_view(request):
    template_page='clinic/our_specialities.html'
    specialities=Speciality.objects.all()
    template_context={
        'specialities':specialities
    }
    return render(request,template_page,context=template_context)