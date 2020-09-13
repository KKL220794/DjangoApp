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
    return render(request, template_name='listings/search.html')
