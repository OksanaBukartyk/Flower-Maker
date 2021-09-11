from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('product/<int:id>/', views.product, name="product"),
    path('product/create/', views.create_product, name="create_product"),
    path('product/edit/<int:id>/', views.edit_product, name='edit_product'),
    path('product/delete/<int:id>/', views.delete_product, name='delete_product'),
    path('product-version/create/<int:id>/', views.create_product_version, name="create_product_version"),
path('product-version/edit/<int:id>/', views.edit_product_version, name='edit_product_version'),
path('product-version/delete/<int:id>/', views.delete_product_version, name='delete_product_version'),
]
