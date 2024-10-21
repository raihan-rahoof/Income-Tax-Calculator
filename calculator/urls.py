from django.urls import path
from .views import TaxCalculatorView

urlpatterns = [
    path("", TaxCalculatorView.as_view(), name="tax_calculator"),
   
]
