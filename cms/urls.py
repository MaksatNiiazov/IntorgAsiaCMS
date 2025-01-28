from django.urls import path
from .views import home_view, calculator_view

urlpatterns = [
    path('', home_view, name='home'),
    path('calculator/', calculator_view, name='calculator'),
]
