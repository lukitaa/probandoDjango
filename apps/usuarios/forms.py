from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
	#La imagen que pertenece a cada usuario
	imagen = forms.FileField()