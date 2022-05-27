# Imports.
from django.urls import path, include
from django.contrib.auth import views as auth_views

# Import my views.
from . import views

# Set the url patterns and the app namespace name.
app_name = 'market'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('listings/', views.ListingsView.as_view(), name='listings'),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='detail'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_request, name='register'),
    path('account/', views.account_details, name='account'),
    path('edit-account-details/', views.edit_account_details, name='edit-account'),
    path('change-password', views.ChangePasswordView.as_view(),
         name='change-password'),
    path('add-item/', views.add_new_item, name='add-item')
]
