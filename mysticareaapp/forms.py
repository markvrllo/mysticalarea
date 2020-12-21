from django import forms
from .models import Cartomante

class Cartomanteform(forms.ModelForm):
	class Meta:
		model = Cartomante
		fields = '__all__'
		