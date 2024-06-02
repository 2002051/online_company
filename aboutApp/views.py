from django.shortcuts import render
from django.shortcuts import HttpResponse


def survey(request):
	return render(request, 'survey.html', {
		'active_menu': 'about',
		'sub_menu': 'survey',
	})


from .models import Award


def honor(request):
	awards = Award.objects.all()
	return render(request, 'honor.html', {
		'active_menu': 'about',
		'sub_menu': 'honor',
		'awards': awards,
	})
