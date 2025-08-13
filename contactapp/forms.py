# forms.py


from django.contrib.auth. forms import UserCreationForm 
from django import forms
from .models import Record

class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required = True,widget=forms.widgets.TextInput(attrs={"placeholder":"First name","class":"form-control"}),label="" )
	last_name = forms.CharField(required = True, widget = forms.widgets.TextInput(attrs={"placeholder":"Type last name", "class":"form-control"}),label="")
	email = forms.CharField(required = True, widget = forms.widgets.TextInput(attrs={"placeholder":"Type valid email", "class":"form-control"}),label="")
	phone = forms.CharField(required = True, widget = forms.widgets.TextInput(attrs={"placeholder":"Type phone number", "class":"form-control"}),label="")

	class Meta:
		model = Record
		exclude = ("user",)
