from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('product/<int:id>/', views.product, name="product"),
    path('product/create',views.create_product,name="create_product"),
    path('product/edit/<int:id>/',views.edit_product,name='edit_product'),
]