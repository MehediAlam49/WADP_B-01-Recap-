from django import forms
from tasks.models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model=TaskModel
        fields='__all__'
        exclude=['Created_by']
        

        widgets={
            'Due_date':forms.DateInput(attrs={'class':'form-control','type':'date',})
        }