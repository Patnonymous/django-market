# Imports.
from django.urls import path

# Import views.
from . import views

# Set the url patterns.
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('listings/', views.ListingsView.as_view(), name='listings')
]
