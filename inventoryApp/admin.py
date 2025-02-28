from django.contrib import admin
from .models import Stock,Category,StockHistory
from .forms import Stock_Create_form

# Register your models here.
class StockCreateAdmin(admin.ModelAdmin):
    list_display=['category','item_name','quantity']
    form=Stock_Create_form
    list_filter=['category']
    search_fields=['category','item_name']


admin.site.register(Stock,StockCreateAdmin)  # StockCreateAdmin  customaized table in admin 
admin.site.register(Category)
admin.site.register(StockHistory)

