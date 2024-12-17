import re
from datetime import datetime
from django.core.exceptions import ValidationError


def model_and_version_validator(value):
    pattern = re.compile(r'[A-Z0-9]{2}')
    if not bool(pattern.match(value)):
        raise ValidationError(
            'Неверный формат введенных данных.'
        )
    
def datetime_validator(value):
    try:
        datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        raise ValidationError('Неверный формат даты и времени. Используйте формат "YYYY-MM-DD HH:MM:SS".')
