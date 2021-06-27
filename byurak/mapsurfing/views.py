from django.shortcuts import render

def depth1(request):
    return render(request, 'surfingmap_depth1.html')

def depth2(request):
    return render(request, 'surfingmap_depth2.html')