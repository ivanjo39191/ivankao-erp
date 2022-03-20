from django.contrib import admin
from django import forms
from django.db.models import Sum
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

# Register your models here.

class RelationalProductInline(admin.TabularInline):
    model = SalesOrder.product.through
    verbose_name = '商品名稱'
    form = RelationalProductForm
    extra = 2
    fields = ('product', 'retail_price', 'number', 'discount','total')
    readonly_fields = ('retail_price', 'total',)
    suit_classes = 'suit-tab suit-tab-general'
    


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):


    def get_sales_volume(self, obj):
        return sum(obj.salesorder_set.through.objects.filter(product=obj).values_list('number', flat=True))
    
    def get_inventory_volume(self, obj):
        return obj.purchase_volume - sum(obj.salesorder_set.through.objects.filter(product=obj).values_list('number', flat=True))
    

    # list_display = ('name', 'retail_price', 'special_price', 'purchase_volume', 'sales_volume', 'inventory_volume')
    list_display = ('name', 'retail_price', 'purchase_volume', 'get_sales_volume', 'get_inventory_volume')
    get_sales_volume.short_description = '銷售量'
    get_inventory_volume.short_description = '庫存量'


@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    
    def get_product(self, obj):
        return "、".join([p.name for p in obj.product.all()])
    
    list_display = ('order_id', 'customer', 'get_product', 'date')
    form = SalesOrderForm
    inlines = [RelationalProductInline,]
    change_form_template = "admin/product/export_changeform.html"
    
    # def response_add(request, obj, post_url_continue=None):
    #     return redirect(f'/product/export/{obj.order_id}')
    
    def response_change(self, request, obj):
        if "_export" in request.POST:
            obj.save()
            return redirect(f'/product/export/?order_id={obj.order_id}')
        return super().response_change(request, obj)

            
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('name', 'tax_id', 'phone', 'address')