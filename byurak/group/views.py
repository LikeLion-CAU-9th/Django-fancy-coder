from django.shortcuts import render
from group.models import Group, GroupNotice
from django.views.generic import View
from group.forms import GroupNoticeForm


def group_detail(request, pk):
    group = Group.objects.get(id=pk)
    users = group.get_users
    mento_users = group.get_mento_users
    mento_users_id = [mento.id for mento in mento_users]
    mentee_users = users

    for mentee_user in mentee_users:
        if mentee_user.id in mento_users_id:
            mentee_users.remove(mentee_user)

    return render(request, 'group_detail.html', {
        "group": group,
        "users": users,
        "mento_users": mento_users,
        "mentee_users": mentee_users
    })


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group_list.html', {"groups": groups})


class GroupNoticeAPIView(View):
    def get_group_queryset(self, pk):
        group = Group.objects.get(id=pk)
        group_notice = GroupNotice.objects.filter(group=group)
        users = group.get_users
        mento_users = group.get_mento_users
        mento_users_id = [mento.id for mento in mento_users]
        mentee_users = users

        for mentee_user in mentee_users:
            if mentee_user.id in mento_users_id:
                mentee_users.remove(mentee_user)

        return {
            "group": group,
            "users": users,
            "mento_users": mento_users,
            "mentee_users": mentee_users,
            "group_notice": group_notice
        }

    def post(self, request, pk):
        group = Group.objects.get(id=pk)
        user = request.user
        group_post_form = GroupNoticeForm()
        group_notice_form = GroupNoticeForm(request.POST)

        if group_notice_form.is_valid():
            notice_instance = group_notice_form.save(commit=False)
            notice_instance.user = user
            notice_instance.group = group
            notice_instance.save()
            return render(request, 'group_detail.html', self.get_group_queryset(pk))
        return render(request, 'group_detail.html', {'post_form': group_post_form})

    def get(self, request, pk):
        return render(request, 'group_detail.html', self.get_group_queryset(pk))
