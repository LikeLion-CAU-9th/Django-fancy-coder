from django.shortcuts import render
from group.models import Group


def group_detail(request, pk):
    group = Group.objects.get(id=pk)
    users = group.get_users
    mento_users = group.get_mento_users
    mento_users_id = [mento.id for mento in mento_users]
    mentee_users = users
    for mentee_user in mentee_users:
        if mentee_user.id in mento_users_id:
            mentee_users.remove(mentee_user)
    # users.exclude(id__in=mento_users_id)
    return render(request, 'group_detail.html', {
        "group": group,
        "users": users,
        "mento_users": mento_users,
        "mentee_users": mentee_users
    })


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group_list.html', {"groups": groups})
