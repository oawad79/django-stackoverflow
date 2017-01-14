#NOTE: refer to http://blog.narenarya.in/right-way-django-authentication.html
#I am using widgets tweaks library instead to customize django form fields using bootstrap with the tweaks library

# from django.contrib.auth.forms import AuthenticationForm
from django import forms
#
#
# # If you don't do this you cannot use Bootstrap CSS
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(label="Username", max_length=30,
#                                widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
#     password = forms.CharField(label="Password", max_length=30,
#                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class ChangePasswordForm(forms.Form):
	newpassword= forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label=("New Password"))
	renewpasssword=forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30)), label=("Retype New Password"))
