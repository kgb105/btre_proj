from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from listings.models import Listing
from django.contrib import messages
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        listing = get_object_or_404(Listing, pk=listing_id)

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You already have requested info on this property')
            else:
                contact = Contact(listing=listing, name = name, email=email, phone=phone, message=message, user_id = user_id)
                contact.save()
                
                send_mail(
                    "Property list Inquiry for property " + listing.title ,
                    "Sign in to view in Admin Panel",
                    'george@rockposters.com.au',
                    ['georgeg@gpl-it.com.au'],
                    fail_silently=False,


                )

                messages.success(request, 'Your request has been submitted')
        

        return redirect('/listings/'+listing_id)