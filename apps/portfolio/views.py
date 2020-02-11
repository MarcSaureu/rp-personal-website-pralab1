from django.shortcuts import render
from apps.portfolio.models import Project

def project_list(request):
	projects = Project.objects.all()

	context = {
		'projects': projects
	}

	return render(request, 'project_list.html', context)
