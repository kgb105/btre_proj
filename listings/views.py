from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from .models import State, Listing, ListingPhoto
from listings.choices import price_choices, bedroom_choices



def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    

    paginator = Paginator(listings, 3)

    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings

    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    photos = ListingPhoto.objects.filter(listing=listing_id)

    context = {
        'listing': listing,
        'photos': photos
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)     

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__code__iexact=state)     

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)    

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)       

    state_choices = State.objects.all()
    context = {
        'listings': queryset_list,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)