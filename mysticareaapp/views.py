from django.shortcuts import render, get_object_or_404,redirect

# Create your views here.
from django.http import HttpResponse
from .forms import Cartomanteform
from .models import Cartomante
from django.contrib import messages
def index(request):
	#return HttpResponse("<h1>Aqui é o index<h1>")
	return render(request, 'cartomantes/index.html')

def cartomantes(request):
	cartomantes = Cartomante.objects.all()
	busca = request.GET.get('search')
	if busca:
		cartomantes = Cartomante.objects.filter(nome_cartomante__icontains = busca)
	return render(request, "cartomantes/cartomantes.html", {'cartomantes':cartomantes})

def editar(request, id):
	cart = get_object_or_404(Cartomante, pk=id)
	form = Cartomanteform(instance = cart)

	if (request.method == "POST"):
		form = Cartomanteform(request.POST, request.FILES, instance = cart)

		if form.is_valid():
			form.save()
			return redirect('cartomantes')
		else:
			return render(request, "cartomantes/editar_cartomantes.html", {'form':form, 'cart':cart})
	else:
		return render(request, "cartomantes/editar_cartomantes.html", {'form':form, 'cart':cart})

def criar_cartomantes(request):
	form = Cartomanteform(request.POST)
	if request.method == "POST":
		form = Cartomanteform(request.POST, request.FILES)
		if form.is_valid():
			hosp = form.save()
			hosp.save()
			messages.success(request, 'Médium registrado com sucesso!')
			form = Cartomanteform()
	return render(request,'cartomantes/criar_cartomantes.html',{'form':form})

def deletar(request, id):
	cart = get_object_or_404(Cartomante, pk=id)

	if (request.method == "POST"):
		cart.delete()
		return redirect('cartomantes')
	return render(request, 'cartomantes/deletar_cartomantes.html', {'cart': cart})