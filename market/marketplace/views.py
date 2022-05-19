# Imports.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User

# Import custom models.
from .models import MarketItem
from .forms import RegisterForm


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


def account_details(request):
    return render(request, template_name='marketplace/base_account.html')


def register_request(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, 'Registration successfull. Welcome to market.')
            return redirect('market:index')
        messages.error(request, 'Registration error. Invalid information.')
    form = RegisterForm()
    return render(request=request, template_name='registration/register.html', context={'register_form': form})


def index(request):
    return HttpResponse("Hello world. You're at the market index.")
