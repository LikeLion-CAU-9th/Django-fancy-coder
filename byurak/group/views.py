from django.shortcuts import render
from group.models import Group

def group_detail(request, pk):
    group = Group.objects.get(id=pk)
    return render(request, 'group_detail.html', {"group": group})


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group_list.html', {"groups":groups})