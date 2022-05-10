"""dishaeyecare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# URLs for Built in Admin
urlpatterns = [
    path('admin/', admin.site.urls),
]

# URLs for the Authentication app
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

# URLs for the Uers app
urlpatterns += [
    path('users/', include('users.urls', namespace='users')),
]

# URLs for Clinic App ( Client )
urlpatterns+=[
    path('', include('clinic.urls', namespace='clinic')),
]

# URLs for Doctor App ( Doctor )
urlpatterns+=[
    path('doctor/', include('doctor.urls', namespace='doctor')),
]

# URLs for Patient App ( Patient )
urlpatterns+=[
    path('patient/', include('patient.urls', namespace='patient')),
]

# URLs for Receptionist App ( Receptionist )
urlpatterns+=[
    path('receptionist/', include('receptionist.urls', namespace='receptionist')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

