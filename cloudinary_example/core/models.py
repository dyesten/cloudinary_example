from django.db import models
from cloudinary.models import CloudinaryField

class Imagens(models.Model):
    imagem = CloudinaryField('imagem')
