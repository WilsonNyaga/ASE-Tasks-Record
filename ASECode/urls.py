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
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),  # Replace 'myapp' with your app's name
]

# urls.py in your app directory
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('all_data/', views.display_all_data, name='display_all_data'),
]

# urls.py in your app directory
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Other URL patterns...
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', auth_views.RegistrationView.as_view(), name='register'),
    # Add other authentication-related URL patterns
]

# urls.py in your app directory
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('contact/', views.contact_view, name='contact'),
]

from django.urls import include
