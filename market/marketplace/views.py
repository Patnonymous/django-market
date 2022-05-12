from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import MarketItem

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'marketplace/index.html'
    context_object_name = 'featured_items_index'

    def get_queryset(self):
        return MarketItem.objects.filter(item_is_featured=True).order_by('-item_date_added')


def index(request):
    return HttpResponse("Hello world. You're at the market index.")
