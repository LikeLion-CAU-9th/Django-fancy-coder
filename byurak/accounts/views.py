from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def producerProfile(request):
    return render(request, 'producerProfile.html')