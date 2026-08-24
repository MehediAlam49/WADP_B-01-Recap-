from django import forms
from formApp.models import *


class productForm(forms.ModelForm):
    class Meta:
        model= productModel
        fields='__all__'
        
        