from django.urls import path
from formApp.views import *

urlpatterns = [
    path('', productList, name='productList'),
    path('add-product/', addProduct, name='addProduct'),
    path('edit-product/<str:p_id>', editProduct, name='editProduct'),
    path('delete-product/<str:p_id>', deleteProduct, name='deleteProduct'),
]
