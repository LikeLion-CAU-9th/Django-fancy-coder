from django.shortcuts import render


def service_landing(request):
    return render(request, 'landing.html')