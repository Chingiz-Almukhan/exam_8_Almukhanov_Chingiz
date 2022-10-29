from django import forms

from market.models import Product


class AddEditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'image']
