"""
URL configuration for ASECode project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [
    path('add_aircraft/', views.add_aircraft, name='add_aircraft'),  # URL for adding aircraft
    path('edit_aircraft/<int:aircraft_id>/', views.edit_aircraft, name='edit_aircraft'),  # URL for editing aircraft
    path('all_data/', views.display_all_data, name='aircraft_list'),  # URL for displaying all aircraft data
    path('contact/', views.contact_view, name='contact'),  # URL for displaying the contact form
    path('search_aircraft/', views.search_aircraft, name='search_aircraft'),
]
