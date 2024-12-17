from django.urls import path
from robots.views import add_robot_view


urlpatterns = [
    path('add_robot/', add_robot_view, name='add_robot'),
]
