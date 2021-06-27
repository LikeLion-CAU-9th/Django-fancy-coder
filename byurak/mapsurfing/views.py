from django.shortcuts import render

def depth1(request):
    return render(request, 'surfingmap_depth1.html')

def depth3(request):
    return render(request, 'surfingmap_depth3.html')