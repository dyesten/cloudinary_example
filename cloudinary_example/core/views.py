#from django.shortcuts import render_to_response
from django.shortcuts import render
from cloudinary_example.core.forms import ImagensForm
from cloudinary_example.core.models import Imagens

def galeria(request):
	if request.method == 'POST':
		form = ImagensForm(request.POST, request.FILES)
        #if form.is_valid():
            #form.save()
		for f in request.FILES.getlist('imagens'):
			Imagens(imagem=f).save()

	return render(request, 'galeria.html', {'form':ImagensForm, 'imgs':Imagens.objects.all()})