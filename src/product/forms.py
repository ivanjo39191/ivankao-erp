from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from easy_select2 import Select2

from .models import *

class SalesOrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SalesOrderForm, self).__init__(*args, **kwargs)

    class Meta:
        model = SalesOrder
        fields = '__all__'

        
class RelationalProductForm(forms.ModelForm):
    class Meta:
        model = SalesOrder.product.through
        fields = '__all__'
        fields = ('product', 'number')
        widgets = {'product': Select2(),}
        
    def __init__(self, *args, **kwargs):
        super(RelationalProductForm, self).__init__(*args, **kwargs)

