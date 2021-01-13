from django.shortcuts import render
from django.views.generic import View, TemplateView


# Create your views here.
class HomePage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'index.html')


class AboutPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'about.html')


class ContactPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'contact.html')


class GalleryPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'gallery.html')


class VolunteerPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'volunteer.html')


class CausesPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'causes.html')
