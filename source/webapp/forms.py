from django import forms
from django.forms import widgets


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='Title')
    description = forms.CharField(max_length=40, required=True, label='Author')
    category = forms.CharField(max_length=3000, required=True, label='Text')
    amount = forms.IntegerField (required=True, label = 'Text')
    price = forms.DecimalField(required=True, label='Text')

