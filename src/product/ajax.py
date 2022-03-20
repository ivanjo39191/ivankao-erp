import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product

@csrf_exempt
def get_product_retail_price(request):
    retail_price = {}
    if request.POST:
        name = request.POST.get('name')
        retail_price =  {'retail_price': Product.objects.get(name=name).retail_price}
        return HttpResponse(json.dumps(retail_price), content_type='application/json')
    return HttpResponse(status=500)