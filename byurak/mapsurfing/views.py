from django.shortcuts import render
from django.conf import settings
from accounts.models import Profile

def depth1(request):
    profiles = Profile.objects.filter(user_type=Profile.SERVICE_PROVIDER).exclude(address__isnull=True)
    print(profiles)
    KAKAO_MAP_KEY = getattr(settings, 'KAKAO_MAP_KEY', 'KAKAO_MAP_KEY')
    return render(request, 'surfingmap_depth1.html', {
        'KAKAO_MAP_KEY' : KAKAO_MAP_KEY,
        "profiles": profiles
        })


def depth2(request):
    KAKAO_MAP_KEY = getattr(settings, 'KAKAO_MAP_KEY', 'KAKAO_MAP_KEY')
    return render(request, 'surfingmap_depth2.html', {'KAKAO_MAP_KEY' : KAKAO_MAP_KEY})


def map_search(request):
    if request.method == "POST":
        search_keyword = request.POST.get("search_keyword")

