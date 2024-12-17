import tempfile
from datetime import datetime, timedelta

from openpyxl import Workbook

from robots.models import Robot
from robots.validators import model_and_version_validator, datetime_validator


def create_robot(data):

    model = data.get('model')
    version = data.get('version')

    model_and_version_validator(model)
    model_and_version_validator(version)
    datetime_validator(data.get('created'))

    data['serial'] = f'{model}-{version}'

    new_robot = Robot(**data)
    new_robot.save()

    return new_robot

def create_excel_table():
    start_search = datetime.now() - timedelta(days=7)
    queryset = Robot.objects.filter(created__gte=start_search).order_by('serial')

    wb = Workbook()
    first_page = wb.active
    cur_page = first_page
    cur_model = None
    cur_serial = None
    cur_serial_data = dict()

    for robot in queryset:

        if not cur_serial:
            cur_serial_data['model'] = robot.model
            cur_serial_data['version'] = robot.version
            cur_serial_data['count'] = 0
            cur_serial = robot.serial

        if cur_serial == robot.serial:
            cur_serial_data['count'] += 1
        else:
            cur_page.append(list(cur_serial_data.values()))
            cur_serial_data['model'] = robot.model
            cur_serial_data['version'] = robot.version
            cur_serial_data['count'] = 1
            cur_serial = robot.serial

        if cur_model != robot.model:
            if cur_model:
                cur_page = wb.create_sheet(title=robot.model)
            cur_page.title = robot.model
            cur_model = robot.model
            cur_page.append(['Модель', 'Версия', 'Количество за неделю'])
            
    cur_page.append(list(cur_serial_data.values()))

        

    temp_file = tempfile.NamedTemporaryFile(delete=False)
    wb.save(temp_file.name)
    return temp_file