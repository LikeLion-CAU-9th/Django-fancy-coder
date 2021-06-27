from django.shortcuts import render
from django.conf import settings
def depth1(request):
    KAKAO_MAP_KEY = getattr(settings, 'KAKAO_MAP_KEY', 'KAKAO_MAP_KEY')
    return render(request, 'surfingmap_depth1.html', {'KAKAO_MAP_KEY' : KAKAO_MAP_KEY})

def depth2(request):
    KAKAO_MAP_KEY = getattr(settings, 'KAKAO_MAP_KEY', 'KAKAO_MAP_KEY')
    return render(request, 'surfingmap_depth2.html', {'KAKAO_MAP_KEY' : KAKAO_MAP_KEY})
