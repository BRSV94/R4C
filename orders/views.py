import json
from datetime import datetime

from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from orders.utils import create_order


@csrf_exempt
@require_http_methods(["POST"])
def add_order_view(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)

    try:
        create_order(data)
        return HttpResponse("Заказ успешно оформлен.")
    except:
        HttpResponseBadRequest()
