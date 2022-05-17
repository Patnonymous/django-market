from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import MarketItem

# Create your views here.


class IndexView(generic.ListView):
    """
    Display special admin featured items.
    """
    template_name = 'marketplace/base_featured.html'
    context_object_name = 'item_listings'

    def get_queryset(self):
        return MarketItem.objects.filter(item_is_featured=True).order_by('-item_date_added')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_header'] = 'Featured Market Items'
        return context


class ListingsView(generic.ListView):
    """
    Display all user items, AKA items that are not featured.
    """
    template_name = 'marketplace/base_user_listings.html'
    context_object_name = 'item_listings'

    def get_queryset(self):
        return MarketItem.objects.filter(item_is_featured=False).order_by('-item_date_added')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_header'] = 'User Market Listings'
        return context


class ItemDetailView(generic.DetailView):
    model = MarketItem
    template_name = 'marketplace/item_detail.html'


def index(request):
    return HttpResponse("Hello world. You're at the market index.")
