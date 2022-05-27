# Imports.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView

# Import custom models.
from .models import MarketItem
from .forms import RegisterForm, EditAccountDetailsForm


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


def add_new_item(request):
    return render(request, 'marketplace/base_add_item.html')


def account_details(request):
    return render(request, 'marketplace/base_account.html')


def register_request(request):
    """
    Register a new account using the form data provided in the request.
    """
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('market:index')
    return render(request, 'registration/register.html', context={'register_form': form})

    # if request.method == 'POST':
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         return redirect('market:index')
    #     else:
    #         print(form.errors)
    # form = RegisterForm()
    # return render(request, template_name='registration/register.html', context={'register_form': form})


def edit_account_details(request):
    # Process forms data on POST.
    form = EditAccountDetailsForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('market:account')
    return render(request, 'marketplace/base_account_edit.html', {'edit_account_form': form})

    # if request.method == 'POST':
    #     print("Request is post.")
    #     form = EditAccountDetailsForm(request.POST)
    #     print(form)
    #     if form.is_valid():
    #         print("Form is valid.")
    #         return redirect('market:account')
    # else:
    #     print("Invalid form.")
    #     form = EditAccountDetailsForm()
    # return render(request, 'marketplace/base_account_edit.html', {'edit_account_form': form})


class ChangePasswordView(PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_url = 'account'

# def change_password(request):
#     form = ChangePasswordForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('market:account')
#     return render(request, 'registration/change_password.html', {'change_password_form': form})


def index(request):
    return HttpResponse("Hello world. You're at the market index.")
