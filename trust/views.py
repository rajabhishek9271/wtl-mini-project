from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from . import mailHandler 
from django.contrib import messages
from . import models
from django.http import HttpResponseRedirect, HttpResponse


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

    def post(self, request, *args, **kwargs):
        form = request.POST
        name = form.get('name')
        email = form.get('email')
        query = form.get('query')

        new_contact = models.Contact.objects.create(
                            name = name,
                            email = email,
                            query=query,

                        )

        new_contact.save()

        mailHandler.sendMailToUser(name, email)
        mailHandler.sendMailToCharity(name, email, message)
        return redirect("contact")

class GalleryPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'gallery.html')


class VolunteerPage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'volunteer.html')
    
    def post(self, request, *args, **kwargs):
         form = request.POST
         name = form.get('name')
         email = form.get('email')
         gender = form.get('gender')
         contact = form.get('contact')
         occupation = form.get('occupation')
         city = form.get('city')
         zipcode = form.get('zipcode')
         reason = form.get('reason')

         new_Volunteer = models.Volunteer.objects.create(
                            name = name,
                            email = email,
                            gender = gender,
                            contact = contact,
                            occupation = occupation,
                            city = city,
                            zipcode = zipcode,
                            reason = reason,                            
                            
         )

         new_Volunteer.save()




class CausesPage(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'causes.html')
