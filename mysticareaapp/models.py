from django.db import models
from PIL import Image

# Create your models here.
class Cartomante(models.Model):
	"""Representa a entidade cartomante"""
	nome_cartomante = models.CharField(max_length=200)
	foto = models.ImageField(null=True, blank=True)
	desc_cartomante = models.TextField(max_length=200)
	tipo_cartomante = models.CharField(max_length=200)
	conceito_cartomante = models.CharField(max_length=200)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		im = Image.open(self.foto.path)
		novo_tamanho = (250,250)
		im.thumbnail(novo_tamanho)
		im.save(self.foto.path)

	def foto_url(self):
		if self.foto and hasattr(self.foto, 'url'):
			print("a url da foto é:", self.foto.url)
			return self.foto.url
		else:
			return "/static/img/36687.jpg"
	
	def __str__(self):
		"""retorna a representação em string do modelo inserido"""
		return self.nome_cartomante