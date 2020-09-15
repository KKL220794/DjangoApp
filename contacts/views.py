from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
# Create your views here.


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        contact = Contact(listing = listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        # check if user has made entry
        if request.user.is_authenticated:
            user_id = request.POST['user_id']
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made a enquiry for this listing')
                return redirect('/listings/' + listing_id)
                
        contact.save()
        # send_mail(
        #             'Property listing enquiry',
        #             'There has been a inquiry for ' + listing + '. sign in into the admin panel for info ' ,
        #             'test@gmail.com',
        #             [realtor_email, 'test@email.com'],
        #             fail_silently=False,
        #         )
        messages.success(request, 'Request submitted. Team will get back to you shortly')
        return redirect('/listings/' + listing_id)
