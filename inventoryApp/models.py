from django.db import models
# Create your models here.
category_choise=(
      ('Furniture','Furniture'),
      ('IT Equipment','IT Equipment'),
      ('Phone','Phone'),
      ('Electronic','Electronic')
)

class Category(models.Model):
      name=models.CharField(max_length=50,blank=True,null=True)
      def __str__(self):
            return self.name

class Stock(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True) 
    item_name=models.CharField(max_length=50,blank=True,null=True)
    quantity=models.IntegerField(default=0,blank=True,null=True)
    received_by=models.CharField(max_length=50,blank=True,null=True)
    received_quantity=models.IntegerField(default=0,blank=True,null=True)
    issue_quantity=models.IntegerField(default=0,blank=True,null=True)
    issue_by=models.CharField(max_length=50,blank=True,null=True)
    issue_to=models.CharField(max_length=50,blank=True,null=True)
    phone_number=models.IntegerField(blank=True,null=True)
    created_by=models.CharField(max_length=50,blank=True,null=True)
    reorder_level=models.IntegerField(default=0,blank=True,null=True)
    last_update=models.DateTimeField(auto_now_add=False,auto_now=True)
    timestamp=models.DateField(auto_now_add=True, auto_now=False)
   #date=models.DateField(auto_now_add=False, auto_now=False)
   

def __str__(self):
        return self.item_name+' '+str(self.quantity)
  
  
class StockHistory(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True, null=True) 
    item_name=models.CharField(max_length=50,blank=True,null=True)
    quantity=models.IntegerField(default=0,blank=True,null=True)
    received_by=models.CharField(max_length=50,blank=True,null=True)
    received_quantity=models.IntegerField(default=0,blank=True,null=True)
    issue_quantity=models.IntegerField(default=0,blank=True,null=True)
    issue_by=models.CharField(max_length=50,blank=True,null=True)
    issue_to=models.CharField(max_length=50,blank=True,null=True)
    phone_number=models.IntegerField(blank=True,null=True)
    created_by=models.CharField(max_length=50,blank=True,null=True)
    reorder_level=models.IntegerField(default=0,blank=True,null=True)
    last_update=models.DateTimeField(auto_now_add=False,auto_now=False , null=True)
    timestamp=models.DateField(auto_now_add=False, auto_now=False, null=True)
   #date=models.DateField(auto_now_add=False, auto_now=False)
   

def __str__(self):
        return self.item_name+' '+str(self.quantity)
    
  
    
