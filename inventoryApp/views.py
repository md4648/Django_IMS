from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Stock_Create_form, Stock_Search_Form
from .models import Stock
# Create your views here.


def Home(request):

    form=Stock_Search_Form(request.POST or None)

    queryset=Stock.objects.all()
    context={'item':queryset,   'form':form}

    if request.method=="POST":
        queryset=Stock.objects.filter(category__icontains=form['category'].value(),
                                      item_name__icontains=form['item_name'].value())
        
        context={
            'item': queryset,   'form':form }

    return render(request,'index.html',context=context)






def addItems(request):
    
    form=Stock_Create_form()
    if request.method=='POST':
        form=Stock_Create_form(request.POST)
        
        if form.is_valid:
            form.save()
            return redirect('')
        
    context={'form':form}
    return render(request,'add-item.html',context=context)
        
    