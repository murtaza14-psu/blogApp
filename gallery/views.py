from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm  

# the product list function fetches all the 
# the data form the database and passes the list in the form of a key value pair 
# to the html and returns the rendered html to browser

def product_list(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

#django automatically generates the pk column
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        #"instance=product" means this form is linked to the existing product
        form = ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            print(form.errors)
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete.html', {'product': product})


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'index2.html', {'product': product})


def home(request):
    return HttpResponse('Hello, World!')