"""
URL configuration for mv_academy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from mv_academy import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('main/', views.main, name='main'),
    path('user-login/', views.login_user, name='user_login'),
    path('user-logout/', views.logout_user, name='user_logout'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('register/', views.register_user, name='user_register'),
    path('about-us/', views.aboutus, name='about_us'),  
    path('contact-us/', views.contactus, name='contact_us'),
    path('gallery/', views.gallery, name='gallery'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
