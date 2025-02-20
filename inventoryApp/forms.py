
from django import forms
from .models import Stock



class Stock_Create_form(forms.ModelForm):

    class Meta:

        model = Stock
        fields = ['category','item_name','quantity']


class Stock_Search_Form(forms.ModelForm):
    class Meta:

        model=Stock
        fields=['category','item_name']
    
    

    

