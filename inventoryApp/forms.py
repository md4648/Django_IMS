
from django import forms
from .models import Stock,StockHistory



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
        
class ReceiveForm(forms.ModelForm):
    class Meta:
        
        model=Stock
        fields=['received_quantity']
        
        
class IssueForm(forms.ModelForm):
    class Meta:
        
        model=Stock
        fields=['issue_by','issue_quantity']


class ReorderForm(forms.ModelForm):
    class Meta:

        model=Stock
        fields=['reorder_level']
        
class StockHistorySearchForm(forms.ModelForm):
    export_to_CSV=forms.BooleanField(required=False)
    start_date=forms.DateTimeField(required=False)
    end_date=forms.DateTimeField(required=False)
    class Meta:
        model=StockHistory
        fields=['category','item_name','start_date','end_date']
        
        
        
        
        


        
    
    

    

