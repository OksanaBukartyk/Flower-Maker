from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from .forms import ProductCreateForm, ProductVersionCreateForm
from .models import *


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'app/index.html', context)


def product(request, id):
    product = Product.objects.get(id=id)
    versions=Version.objects.filter(product_id=product.id)
    context = {'product': product,'versions':versions}
    return render(request, 'app/product.html', context)


def create_product(request):
    product_form = ProductCreateForm( request.POST,request.FILES)
    version_form = ProductVersionCreateForm(request.POST,request.FILES)
    messages.error(request, 'Не 1111')
    if product_form.is_valid() and version_form.is_valid():
        product = product_form.save()
        version = version_form.save(commit=False)
        version.product_id = product
        version.save()

        messages.error(request, 'Не вірний 222')
        return redirect('index')
    else:
        product_form = ProductCreateForm()
        version_form = ProductVersionCreateForm( )
        messages.error(request, 'Не вірний 333')
    return render(request, "app/product_create_form.html", {'product_form': product_form,
                                                            'version_form': version_form,
                                                            })
def edit_product(request, id):
    product = Product.objects.get(id=id)
    product_form=ProductCreateForm(instance=product)
    if request.method == 'POST':
        form=ProductCreateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
        return redirect('index')
    context = {'product_form': product_form}
    return render(request, 'app/product_create_form.html',context)

