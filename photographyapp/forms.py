from .models import shop
from django import forms


class ModelForm(forms.ModelForm):
    class Meta:
        model = shop
        fields = ['name', 'img', 'location', 'price']
