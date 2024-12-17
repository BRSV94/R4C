import json
from datetime import datetime

from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from robots.utils import create_robot, create_excel_table


@csrf_exempt
@require_http_methods(["POST"])
def add_robot_view(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)
    new_robot = create_robot(data)
    return JsonResponse(model_to_dict(new_robot))

@csrf_exempt
@require_http_methods(["GET"])
def export_data_view(request):
    excel_file_path = create_excel_table()
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    )
    file_name = f'robots {datetime.now()}'[:17]
    response['Content-Disposition'] = f'attachment; filename="{file_name}.xlsx"'
    with open(excel_file_path.name, 'rb') as excel_file:
        response.write(excel_file.read())
    excel_file_path.close()

    return response
