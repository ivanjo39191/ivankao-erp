from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

__all__ = ('Product', 'ProductType', 'SalesOrder', 'RelationalProduct')

class SalesOrder(TimeStampedModel):
    order_id = models.CharField('出貨單號', max_length=191, db_index=True, null=True, blank=True) # Order ID
    customer = models.ForeignKey('product.Customer', blank=True, null=True, on_delete=models.CASCADE, related_name='salesorder_set')
    product = models.ManyToManyField('product.Product', blank=True, related_name='salesorder_set', through='product.RelationalProduct') 
    date = models.DateField('出貨日期', null=True, blank=True)  # 出貨日期
    
    def __str__(self):
        return self.order_id



# Create your models here.
class ProductType(TimeStampedModel):
    type_name = models.CharField(max_length=200, null=True)
    order = models.PositiveIntegerField(_('Order'), null=True, blank=True, default=None)

    def __str__(self):
        return self.type_name

    class Meta:
        ordering = ['order','type_name']

class RelationalProduct(TimeStampedModel):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='商品名稱')
    sales_order = models.ForeignKey('product.SalesOrder', on_delete=models.CASCADE)
    number = models.IntegerField('數量', default=1)
    discount = models.IntegerField('折扣 % off', default=0)
    
    def __str__(self):
        return ""

    @property
    def retail_price(self):
        return self.product.retail_price
    retail_price.fget.short_description = '零售價'

    @property
    def total(self):
        retail_price = int(self.number)*int(self.product.retail_price)
        total = "%d" % (int(retail_price)*((100-int(self.discount))/100) if self.discount else int(retail_price))
        return total
    
class Product(TimeStampedModel):

    name = models.CharField(max_length=200, null=True)
    retail_price = models.CharField('零售價', max_length=200, null=True)
    # special_price = models.CharField(max_length=200, null=True)
    purchase_volume = models.IntegerField('進貨量', default=0)
    # sales_volume = models.IntegerField('銷售量', default=0)
    # inventory_volume = models.IntegerField('庫存量', default=0)
    

    
    def __str__(self):
        return self.name

