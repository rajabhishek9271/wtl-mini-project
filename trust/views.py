from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from . import mailHandler
from django.contrib import messages
from . import models
from charity import sheets
from django.http import HttpResponseRedirect, HttpResponse
from trust.paytm import PaytmChecksum
from django.views.decorators.csrf import csrf_exempt
import uuid



MERCHANT_KEY = '0imgPkKAzYEJLh4E'
MERCHANT_ID = 'hPXFbH72610172352610'


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
        mailHandler.sendMailToCharity(name, email, query)
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

         insertRow = ["name","email","gender","contact","occupation","city","zipcode","reason"]

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
         sheets.Volunteer(name,email,gender,contact,occupation,city,zipcode,reason)
         return render(request, 'volunteer.html')



class CausesPage(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'causes.html')


class DonatePage(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'donate.html')


    def post(self, request, *args, **kwargs):
        form = request.POST


        if "submit1" in form:

            request.session['isRegularDonator'] = True

            fname = form.get('fname')
            lname = form.get('lname')
            email = form.get('email')
            gender = form.get('gender')
            contact = form.get('contact')
            occupation = form.get('occupation')
            city = form.get('city')
            zipcode = form.get('zipcode')
            type = form.get('type')
            amount = None
            insertRow = ["name","email","gender","contact","occupation","city","zipcode","reason"]

            if type == "Money":
                amount = form.get('amount')
            new_reg_donater = models.Regulardonation.objects.create(
                        id=uuid.uuid4(),
                        fname=fname,
                        lname=lname,
                        email=email,
                        gender=gender,
                        contact=contact,
                        occupation=occupation,
                        city=city,
                        zipcode=zipcode,
                        type=type,
                        amount=amount,

                    )
            name = f"{fname} {lname}"
            # mailHandler.sendMailToRegularDonator(fname, amount, email)
            # mailHandler.sendMailToTravancoreRegularDonation(fname, lname, email, gender, contact, occupation, city, zipcode, type)
            # messages.success(request, "Your volunteer form details has been successfully submitted. We will get back to you soon.")
            request.session['id'] = str(new_reg_donater.id)

            if type == "Money":

                return HttpResponseRedirect('/payment/')
            else:
                context = {
                'submitted':True
                }
                sheets.RegularDonation(name, email, contact, gender, occupation, city, zipcode, type, amount)

                return render(request, 'index.html', context=context)



            # ----------Anonymous Donation------------
        elif "submit2" in form:

            request.session['isRegularDonator'] = False

            zipcode = form.get('zipcode')
            type = form.get('type')
            amount = None
            if type == "Money":
                amount = form.get('amount')

            new_anony_donater = models.Anonymousdonation.objects.create(
                        id=uuid.uuid4(),
                        zipcode=zipcode,
                        type=type,
                        amount=amount,

                    )

            request.session['id'] = str(new_anony_donater.id)

            if type == "Money":

                request.session['email'] = form.get('email')

                return HttpResponseRedirect('/payment/')

            else:
                sheets.AnonymousDonation(zipcode, type, amount)

                context = {
                'submitted':True
                }

                return render(request, 'index.html', context=context)

            # mailHandler.sendMailToTravancoreIrregularDonation(zipcode, amount, type)
            # messages.success(request, "Your volunteer form details has been successfully submitted. We will get back to you soon.")



class PaytmView(TemplateView):
    template_name = 'payment/paytm.html'

def payment_view(request):

    try:

        isRegularDonator = request.session['isRegularDonator']
        current_donator = None
        CALLBACK_URL = ""
        if "www" in str(request.META['HTTP_HOST']):
            CALLBACK_URL = "http://127.0.0.1:8000/handle_request/"
        else:
            CALLBACK_URL = "http://127.0.0.1:8000/handle_request/"


        if (isRegularDonator):
            current_donator = models.Regulardonation.objects.get(id=request.session['id'])
            param_dict={
                        'MID':MERCHANT_ID,
                        'ORDER_ID':str(request.session['id']),
                        'TXN_AMOUNT':str(current_donator.amount),
                        'CUST_ID':current_donator.email,
                        'INDUSTRY_TYPE_ID':'Retail',
                        'WEBSITE':'WEBSTAGING',
                        'CHANNEL_ID':'WEB',
            	        'CALLBACK_URL':CALLBACK_URL,
                    }
        else:
            current_donator = models.Anonymousdonation.objects.get(id=request.session['id'])
            param_dict={
                        'MID':MERCHANT_ID,
                        'ORDER_ID':str(request.session['id']),
                        'TXN_AMOUNT':str(current_donator.amount),
                        'CUST_ID':request.session['email'],
                        'INDUSTRY_TYPE_ID':'Retail',
                        'WEBSITE':'WEBSTAGING',
                        'CHANNEL_ID':'WEB',
            	        'CALLBACK_URL':CALLBACK_URL,
                    }


        param_dict['CHECKSUMHASH'] = PaytmChecksum.generateSignature(param_dict, MERCHANT_KEY)
        return render(request, 'payment/paytm.html', {'param_dict':param_dict})
    except:
        return render(request, 'error/404.html')

@csrf_exempt
def handle_request(request):

    if request.method == "POST":

        # import checksum generation utility
        paytmChecksum = ""

    # Create a Dictionary from the parameters received in POST
    # received_data should contains all data received in POST
        form = request.POST
        paytmParams = {}

        for i in form.keys():
            paytmParams[i] = form[i]
            if i == 'CHECKSUMHASH':
                checksum = form[i]
        # Verify checksum
        # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
        isValidChecksum = PaytmChecksum.verifySignature(paytmParams, MERCHANT_KEY, checksum)
        # if isValidChecksum:
	    #     if paytmParams['RESPCODE'] == '01':
        #         pass

        return render(request, 'payment/payment_status.html', {'response':paytmParams})
    else:

        return render(request, 'error/404.html')

def after_payment(request):

    if request.method == "POST":

        # Successfull payment
        if request.POST.get('respcode') == '01':


            if(request.session['isRegularDonator']):

                current_donator = models.Regulardonation.objects.get(id=request.session['id'])

                name = f"{current_donator.fname} {current_donator.lname}"

                # Add Regular Donation entry to Google sheet
                sheets.RegularDonation(
                name, current_donator.email, current_donator.contact,
                current_donator.gender, current_donator.occupation, current_donator.city,
                current_donator.zipcode, current_donator.type, current_donator.amount, request.POST.get('bankid')
                )

            else:
                current_donator = models.Anonymousdonation.objects.get(id=request.session['id'])

                # Add Anonymous Donation entry to Google sheet

                sheets.AnonymousDonation(current_donator.zipcode, current_donator.type, current_donator.amount, request.POST.get('bankid'))
                del request.session['email']


            context={
                'status':True,
                'order_id':request.POST.get('order_id'),
                'response':request.POST.get('response'),
                'txn_amount':request.POST.get('txn_amount'),
                'banktxnid':request.POST.get('bankid')
            }
            del request.session['id']
            del request.session['isRegularDonator']

            return render(request, 'payment/payment-complete.html', context)

        # Unsucessful payment
        else:
            if(request.session['isRegularDonator']):
                del request.session['id']
            else:
                del request.session['id']
                del request.session['email']
            del request.session['isRegularDonator']

            context={
                'status':False,
                'order_id':request.POST.get('order_id'),
                'response':request.POST.get('response'),
                'txn_amount':request.POST.get('txn_amount'),
                'banktxnid':request.POST.get('bankid')
            }
            return render(request, 'payment/payment-complete.html', context)
    else:
        return render(request, 'error/404.html')

def handler404(request, exception):

    return render(request, 'error/404.html')
