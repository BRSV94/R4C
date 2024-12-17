import re
from django.core.exceptions import ValidationError


def serial_validator(value):
    pattern = re.compile(r'^[A-Z0-9]{2}-[A-Z0-9]{2}$')
    if not bool(pattern.match(value)):
        raise ValidationError(
            'Неверный формат введенных данных.'
        )

