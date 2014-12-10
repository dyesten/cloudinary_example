from django import forms
from cloudinary_example.core.models import Imagens
from cloudinary.forms import CloudinaryJsFileField

class ImagensForm(forms.ModelForm):
	class Meta:
		model = Imagens
	imagem = CloudinaryJsFileField( attrs={'multiple': 1, 'name':'imagens'} )