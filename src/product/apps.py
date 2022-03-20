from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

class ProductConfig(AppConfig):
    name = 'product'
    verbose_name = _('Product')

    menu = [
        ParentItem(verbose_name, children=[
            ChildItem(model='product.product'),
            ChildItem(model='product.salesorder'),
            ChildItem(model='product.customer'),
        ], icon='fa fa-table'),
    ]
