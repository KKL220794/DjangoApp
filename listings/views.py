from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing
# Create your views here.


def index(request):
    return render(request, 'listings/listings.html')

 
def listing(request):
    return render(request, template_name='listings/listing.html')

def search(request):
    return render(request, template_name='listings/search.html')
