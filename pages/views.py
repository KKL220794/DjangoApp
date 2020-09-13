from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor


# Create your views here.


def index(request):

    listings = Listing.objects.order_by('-list_date').filter(is_published = True)[:3]
    context = {
        'listings': listings
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtor = Realtor.objects.order_by('-hire_date')
    mvp = Realtor.objects.filter(is_mvp= True )
    context = {
        'realtor': realtor,
        'mvp': mvp
    }
    return render(request, template_name='pages/about.html',context=context)