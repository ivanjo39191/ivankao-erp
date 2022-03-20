from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from .models import SalesOrder, RelationalProduct

# Create your views here.
@method_decorator(never_cache, name='dispatch')
class ExportView(TemplateView):
    template_name = 'product/export.html'

    def get_context_data(self, **kwargs):
        context = super(ExportView, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        if request.GET.get("order_id"):
            order_id = request.GET.get("order_id", '')
            obj = SalesOrder.objects.filter(order_id=order_id).first()
            products = RelationalProduct.objects.filter(sales_order=obj)
            result = []
            for product in products:
                retail_price = int(product.number)*int(product.product.retail_price)
                special_price = "%d" % (int(retail_price)*(int(product.discount)/100) if product.discount else int(retail_price))
                result.append([product.product.name, product.number, retail_price, special_price])
        context = self.get_context_data()
        context['obj'] = obj
        context['result'] = result
        return self.render_to_response(context)