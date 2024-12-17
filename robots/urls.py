from django.urls import path
from robots.views import add_robot_view, export_data_view


urlpatterns = [
    path('add_robot/', add_robot_view, name='add_robot'),
    path('export_data/', export_data_view, name='export_data'),
]
