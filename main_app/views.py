from django.shortcuts import render

from .models import HomefieldModels,HomeViewModel


def HomeView(request):
    home_title = HomeViewModel.objects.all()
    download_cv = HomefieldModels.objects.all()

    context = {
        'home_title':home_title,
        'download_cv':download_cv,
        }

    return render(request,'home.html', context)


def BaseView(request):
    return render(request,'base.html')


def ProjectView(request):
    return render(request,'project.html')


def ResumeView(request):
    return render(request,'resume.html')


def ContactView(request):
    return render(request,'contact.html')
