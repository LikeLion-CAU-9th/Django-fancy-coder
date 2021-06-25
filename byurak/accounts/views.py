from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup_main(request):
    return render(request, 'signup_main.html')

def signup_infor(request):
    return render(request, 'signup_infor.html')