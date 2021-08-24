from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class CreateItemForm(forms.Form):

    title = forms.CharField(max_length=200)
    amount = forms.IntegerField(help_text='Enter what amount of this item would you like to buy.')
    #maybe can check the amount next time
    summary = forms.CharField(max_length=1000, help_text='Enter a brief description of the item.')