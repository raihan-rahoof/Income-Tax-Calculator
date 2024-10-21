from django.shortcuts import render
from django.views import View

from .forms import Taxform
from .services import GenericTaxSlab, IncomeTaxCalculator


class TaxCalculatorView(View):
    template_name = "tax_calculator/tax_calculator_form.html"

    def get(self, request):
        form = Taxform()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = Taxform(request.POST)
        if form.is_valid():
            try:
                income = form.cleaned_data["income"]

                if income < 0:
                    form.add_error("income", "Income Cannot be Negative")
                    return render(request, self.template_name, {"form": form})

                slabs = [
                    GenericTaxSlab(0, 250000, 0),
                    GenericTaxSlab(250000, 500000, 0.05),
                    GenericTaxSlab(500000, 1000000, 0.2),
                    GenericTaxSlab(1000000, None, 0.3),
                ]

                calculator = IncomeTaxCalculator(slabs)
                total_tax = calculator.calculate_total_tax(income)
                slab_details = [
                    {
                        "slab_range": f"{slab.lower_limit} - {slab.upper_limit or 'Above'}",
                        "rate": f"{int(slab.rate * 100)}%",
                        "tax_amount": slab.calculate(income),
                    }
                    for slab in slabs
                ]

                return render(
                    request,
                    "tax_calculator/tax_calculator_results.html",
                    {
                        "income": income,
                        "total_tax": total_tax,
                        "slab_details": slab_details,
                    },
                )
            except Exception as e:
                form.add_error(
                    None, f"An error occurred during tax calculation: {str(e)}"
                )
                return render(request, self.template_name, {"form": form})

        return render(request, self.template_name, {"form": form})
