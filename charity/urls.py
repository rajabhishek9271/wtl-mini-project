"""charity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from trust import views
import trust as tr


handler404 = tr.views.handler404


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage.as_view(),name='index'),
    path('about/',views.AboutPage.as_view(),name='about'),
    path('gallery/',views.GalleryPage.as_view(),name='gallery'),
    path('contact/',views.ContactPage.as_view(),name='contact'),
    path('volunteer/',views.VolunteerPage.as_view(),name='volunteer'),
    path('causes/',views.CausesPage.as_view(),name='causes'),
    path('donate/',views.DonatePage.as_view(),name='donate'),
    path('payment/', views.payment_view, name="payment"),
    path('payment-complete/', views.after_payment, name="payment-complete"),
    path('handle_request/', views.handle_request, name="handle_request"),
]
