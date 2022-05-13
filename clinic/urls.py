from django.urls import path

from .views import home_view,contact_us_view,about_us_view,our_doctors_view,our_specialities_view

app_name = 'clinic'

urlpatterns = [
    path('', home_view, name='home'),
    path('contact-us/', contact_us_view, name='contact-us'),
    path('about-us/', about_us_view, name='about-us'),
    path('our-doctors/', our_doctors_view , name='our-doctors'),
    path('our-specialities/', our_specialities_view , name='our-specialities'),

]
