from django import forms
from .models import *

class vegform(forms.ModelForm):
    class Meta:
        model=Veg
        fields= '__all__'
    #    fields=['name','color']