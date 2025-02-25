from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Stock_Create_form, Stock_Search_Form,Update_Stock_Form,ReceiveForm,IssueForm,ReorderForm
from .models import Stock
from django.http import HttpResponse
from django.contrib import messages
import csv

# Create your views here.


def Home(request):

    form=Stock_Search_Form(request.POST or None)

    queryset=Stock.objects.all()
    context={'item':queryset,   'form':form}

    if request.method=="POST":
        queryset=Stock.objects.filter(#category__icontains=form['category'].value(),
                                      item_name__icontains=form['item_name'].value())
        
        if form['export_to_CSV'].value()==True:
            response=HttpResponse(content_type='text/csv')
            response['Content-Disposition']='attachment; filename="List of stock.csv"'
            writer=csv.writer(response)
            writer.writerow(['CATEGORY','ITEM NAME','QUANTITY'])
            instance=queryset
            for stock in instance:
                writer.writerow([stock.category,stock.item_name,stock.quantity])
            return response

        context={
            'item': queryset,   'form':form }
        
    # print(queryset[1].item_name)

    return render(request,'index.html',context=context)



def addItems(request):
    
    form=Stock_Create_form()
    if request.method=='POST':
        form=Stock_Create_form(request.POST)
        
        if form.is_valid():
            
            form.save()
            messages.success(request,'Item created succssefully')

            return redirect('/')
        
    context={'form':form}
    return render(request,'add-item.html',context=context)


def updateItem(request,pk):
    
    item=Stock.objects.get(id=pk)
    form=Update_Stock_Form(instance=item)
    
    if request.method=="POST":
        form=Update_Stock_Form(request.POST, instance=item)
        
        if form.is_valid():
            form.save()
            messages.success(request,'updated succussefully')
            return redirect('/')
            
    context={'form':form}
    
    return render(request,'update-item.html',context=context)


def delete_item(request,pk):
    queryset=Stock.objects.get(id=pk)
    if request.method=='POST':
        queryset.delete()
        messages.success(request,'Deleted succssefully')
        return redirect('/')
    return render(request, 'delete_item.html')

def stock_detail(request,pk):
    queryset=Stock.objects.get(id=pk)
    
    context={'item':queryset}
    return render(request,'stock_detail.html',context=context)


def receive_item(request,pk):
    
    item=Stock.objects.get(id=pk)
    
    form=ReceiveForm(instance=item)
    
    if request.method=='POST':
        form=ReceiveForm(request.POST or None,instance=item)
        if form.is_valid:
            instancess=form.save(commit=False)
            instancess.quantity+=instancess.received_quantity
            instancess.save()
            messages.success(request,'Quantity is Recived  succussefully')
            # return redirect('/stock_detail/'+str(instancess.id))
            return redirect('/')
            
    context={'form':form}
    return render(request,'receive_item.html',context=context)



def issue_item(request,pk):
    
    item=Stock.objects.get(id=pk)
    
    form=IssueForm(instance=item)
    
    if request.method=='POST':
        form=IssueForm(request.POST or None,instance=item)
        if form.is_valid:
            instancess=form.save(commit=False)
            instancess.quantity-=instancess.received_quantity
            instancess.save()
            messages.success(request,'Quantity is Issued  succussefully')
            # return redirect('/stock_detail/'+str(instancess.id))
            return redirect('/')
            
    context={'form':form}
    return render(request,'issue_item.html',context=context)


def reorder_item(request,pk):

    item=Stock.objects.get(id=pk)

    form=ReorderForm(instance=item)

    if request.method=='POST':
        form=ReorderForm(request.POST or None, instance=item)

        if form.is_valid:
            form.save()
            messages.success(request,'Item is Reorder succussefully')
            return redirect('/')
         
    
    context={'form':form}
    return render(request,'reorder.html',context=context)



    
        
    