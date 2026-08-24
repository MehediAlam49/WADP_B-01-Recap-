from django.shortcuts import render,redirect
from formApp.models import *
from formApp.forms import *

# Create your views here.
def productList(request):
    products=productModel.objects.all()

    context={
        'products':products
    }
    return render(request, 'productList.html',context)


def addProduct(request):
    #to save form data in database
    if request.method=='POST':
        form_data=productForm(request.POST, request.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect('productList')

    #to show the form in html page
    form_data=productForm()
    context={
        'form_data':form_data,
        'form_heading':'Add Product Form',
        'form_btn':'Add Product'
    }
    return render(request, 'master/base-form.html',context)

def editProduct(request,p_id):
    product_data=productModel.objects.get(id=p_id)

    #to update form data in database
    if request.method=='POST':
            form_data=productForm(request.POST, request.FILES, instance=product_data)
            if form_data.is_valid():
                form_data.save()
                return redirect('productList')

    #to show the form in html page
    form_data=productForm(instance=product_data)
    context={
            'form_data':form_data,
            'form_heading':'Edit Product Form',
            'form_btn':'Update'
        }
    return render(request, 'master/base-form.html',context)

def deleteProduct(request, p_id):
     product_data=productModel.objects.get(id=p_id)
     product_data.delete()
     return redirect('productList')