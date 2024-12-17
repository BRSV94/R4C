from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from customers.models import Customer
from orders.models import Order
from orders.validators import serial_validator


def create_order(data):
    customer_id = data.get('customer_id')
    robot_serial = data.get('robot_serial')

    customer = get_object_or_404(Customer, id=customer_id)
    serial_validator(robot_serial)

    new_order = Order(customer=customer, robot_serial=robot_serial)
    new_order.save()


def send_message(model, version, order):
    MESSAGE = f'''
    Добрый день!
    Недавно вы интересовались нашим роботом модели {model}, версии {version}. 
    Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами
    '''
    SUBJECT = 'Робот готов.'
    FROM_EMAIL = 'mymail@gmail.com'
    to_mail = order.customer.email
    
    # Имитирую отправку письма:
    print(
        'ОТПРАВЛЕНО',
        SUBJECT,
        MESSAGE,
        FROM_EMAIL,
        to_mail
    )
    # send_mail(
    #     subject=SUBJECT,
    #     message=MESSAGE,
    #     from_email=FROM_EMAIL,
    #     recipient_list=[to_mail]
    # )

def check_open_order(data):
    model = data.get('model')
    version = data.get('version')
    robot_serial = f'{model}-{version}'
    
    queryset = Order.objects.filter(robot_serial=robot_serial)
    order_exists = queryset.exists()
    
    if order_exists:
        send_message(model, version, queryset.first())
