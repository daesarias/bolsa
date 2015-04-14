from django import forms
from Appi.models import Usuario


class RegistroForm(forms.ModelForm):
	class Meta:
		model = Usuario
		exclude = ['usuario','activo','estado','perfil']
