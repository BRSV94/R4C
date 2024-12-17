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