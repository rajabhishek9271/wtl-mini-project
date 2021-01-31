from django.contrib import admin
from .models import Volunteer, Contact, Regulardonation, Anonymousdonation

# Register your models here.

admin.site.register(Volunteer)
admin.site.register(Contact)
admin.site.register(Regulardonation)
admin.site.register(Anonymousdonation)
