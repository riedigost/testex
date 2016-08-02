from django.shortcuts import render, get_object_or_404
from app.models import Client, Provider, Region

def index(request):
	"""Представление главной страницы"""
	return render(request, 'index.html')

def search(request):
	"""Представление результата поиска"""
	q = request.GET['q']
	regions = Region.objects.filter(client__name__iexact=q).values_list('id', flat=True)
	providers = Provider.objects.filter(regions__id__in=regions).distinct()

	return render(request, 'result.html', 
		{'providers': providers, 'query': q})

def detail(request, provider_id):
	"""Представление личной страницы поставщика"""
	provider = get_object_or_404(Provider, pk=provider_id)
	regions = Region.objects.filter(provider__id__exact=provider_id)

	return render(request, 'detail.html', 
		{'provider': provider, 'regions': regions})