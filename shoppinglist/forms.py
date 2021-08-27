from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class CreateItemForm(forms.Form):

    title = forms.CharField(max_length=200)
    amount = forms.IntegerField(help_text='Enter what amount of this item would you like to buy.')
    #maybe can check the amount next time
    summary = forms.CharField(max_length=1000, help_text='Enter a brief description of the item.')

# for user registration
# Source: https://www.ordinarycoders.com/blog/article/django-user-register-login-logout

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user