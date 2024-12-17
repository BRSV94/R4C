import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from robots.utils import create_robot


@csrf_exempt
def add_robot_view(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)
    new_robot = create_robot(data)
    return JsonResponse(model_to_dict(new_robot))
