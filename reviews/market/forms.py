from django import forms

from market.models import Product, Review


class AddEditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'image']


class AddEditReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review', 'grade']
