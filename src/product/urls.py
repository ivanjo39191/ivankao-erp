from django.urls import path
from . import views, ajax

app_name = 'product'
urlpatterns = [
    path('export/', views.ExportView.as_view(), name='export'),
    path('get_product_retail_price/', ajax.get_product_retail_price, name='get_product_retail_price'),
]
