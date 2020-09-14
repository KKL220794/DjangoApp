from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Listing
from django.core.paginator import Paginator, EmptyPage
# Create your views here.


def index(request):

    listing = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listing,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listing': paged_listings
    }

    return render(request, 'listings/listings.html', context )

 
def listing(request, listing_id):

    listing = get_object_or_404(Listing, pk = listing_id)
    context = {
        'listing' : listing
    }
    return render(request, template_name='listings/listing.html', context=context)

def search(request):

    filtered_listing = Listing.objects.order_by('-list_date')
    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            filtered_listing = filtered_listing.filter(description__icontains = keywords)

        # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            filtered_listing = filtered_listing.filter(city__iexact=city)
            

        # state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            filtered_listing = filtered_listing.filter(state__iexact=state)

    # bedroom
    if 'bedrooms' in request.GET:
        bedroom = request.GET['bedrooms']
        if bedroom:
            filtered_listing = filtered_listing.filter(bedrooms__lte=bedroom)

    # price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            filtered_listing = filtered_listing.filter(price__lte=price)

    context = {
        'listing':filtered_listing,
        'values': request.GET
    }
    return render(request, template_name='listings/search.html', context=context)
