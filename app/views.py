from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *
# Create your views here.
def home(request):
    products=Product.objects.all()
    context={'products':products}

    return render(request, 'app/index.html',context)
