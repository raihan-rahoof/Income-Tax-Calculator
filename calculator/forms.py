from django import forms

class Taxform(forms.Form):
    income = forms.FloatField(label="Enter Your Taxable Income",min_value=0)