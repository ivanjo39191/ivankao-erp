import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product

@csrf_exempt
def get_product_retail_price(request):
    retail_price = {}
    if request.POST:
        name = request.POST.get('name')
        if retail_price_obj := Product.objects.filter(name=name):
            retail_price = retail_price_obj.first().retail_price
        else:
            retail_price = 0
        retail_price_dict = {'retail_price': retail_price}
        return HttpResponse(json.dumps(retail_price_dict), content_type='application/json')
    return HttpResponse(status=500)