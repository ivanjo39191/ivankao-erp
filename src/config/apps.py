from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

from product.apps import ProductConfig

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
    menu = ProductConfig.menu