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
    product_form = ProductCreateForm( request.POST,request.FILES or None)
    version_form = ProductVersionCreateForm(request.POST,request.FILES)
    if product_form.is_valid() and version_form.is_valid():
        product = product_form.save()
        version = version_form.save(commit=False)
        version.product_id = product
        version.save()
        messages.error(request, 'Вітаю, ви добавили новий товар')
        return redirect('index')
    #else:
       # product_form = ProductCreateForm()
       # version_form = ProductVersionCreateForm( )

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

def delete_product(request,id):
    product=Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        versions=Version.objects.filter(product_id=product)
        versions.delete()
        return redirect('index')
    context = {'item':product}
    return render(request, 'app/product_delete_form.html', context)


def create_product_version(request,id):
    version_form = ProductVersionCreateForm(request.POST,request.FILES)
    product=Product.objects.get(id=id)
    if version_form.is_valid():
        version = version_form.save(commit=False)
        version.product_id = product
        version.save()
        messages.error(request, 'Вітаю ви добавили новий варінт товару!')
        return redirect('product', id=version.product_id.id)
    #else:
        #product_form = ProductCreateForm()
        #version_form = ProductVersionCreateForm( )

    return render(request, "app/product_create_form.html", {'version_form': version_form,
                                                            })
def edit_product_version(request,id):
    version = Version.objects.get(id=id)
    version_form = ProductVersionCreateForm(instance=version)
    if request.method == 'POST':
        form = ProductVersionCreateForm(request.POST, request.FILES, instance=version)
        if form.is_valid():
            form.save()
        return redirect('product', id=version.product_id.id)
    context = {'product_form': version_form}
    return render(request, 'app/product_create_form.html', context)

def delete_product_version(request,id):
    version=Version.objects.get(id=id)
    if request.method == 'POST':
        version.delete()
        return redirect('product', id=version.product_id.id)
    context = {'item':version}
    return render(request, 'app/product_delete_form.html', context)
