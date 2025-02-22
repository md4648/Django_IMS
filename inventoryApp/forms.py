
from django import forms
from .models import Stock



class Stock_Create_form(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ['category','item_name','quantity']
        
    def clean_category(self):
        Fcategory=self.cleaned_data.get('category')
        if not Fcategory:
            raise forms.ValidationError('This Field is Required!')
        
        for instance in Stock.objects.all():
            if instance.category==Fcategory:
                raise forms.ValidationError(instance.category+' is Already Exist!')
            
        return Fcategory
    
    def clean_item_name(self):
        Fitem_name=self.cleaned_data.get('item_name')
        
        if not Fitem_name:
            raise forms.ValidationError('This Field is Required! ')
        
        for instance in Stock.objects.all():
            if instance.item_name==Fitem_name:
                raise forms.ValidationError(instance.item_name+' is Already Exist')
            
        return Fitem_name
            
        
class Stock_Search_Form(forms.ModelForm):
    export_to_CSV=forms.BooleanField(required=False)
    class Meta:

        model=Stock
        fields=['category','item_name']
        
        
        
class Update_Stock_Form(forms.ModelForm):
    class Meta:

        model=Stock
        fields=['category','item_name','quantity']
        
        
        
        
        


        
    
    

    

