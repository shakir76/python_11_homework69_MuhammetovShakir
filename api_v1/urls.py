from django.urls import path

from api_v1.views import add_view, subtract_view, multiply_view, divide_view

app_name = 'api_v1'

urlpatterns = [
    path('add/', add_view),
    path('subtract/', subtract_view),
    path('multiply/', multiply_view),
    path('divide/', divide_view),
]
