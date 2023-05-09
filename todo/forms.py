from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    # inner class gives form info about itself
    class Meta:
        model = Item
        fields = ['name', 'done']
