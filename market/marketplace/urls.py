# Imports.
from django.urls import path

# Import views.
from . import views

# Set the url patterns and the app namespace name.
app_name = 'market'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('listings/', views.ListingsView.as_view(), name='listings'),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='detail')
]
