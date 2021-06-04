from django import forms
from group.models import GroupNotice

class GroupNoticeForm(forms.ModelForm):
    class Meta:
        model = GroupNotice
        fields = ('title', 'body')

    def validate_title(self):
        title = self.cleaned_data.get('title')

        if title is None:
            raise forms.ValidationError('Title is None.')
        else:
            return title

    def validate_body(self):
        body = self.cleaned_data.get('body')

        if body is None:
            raise forms.ValidationError('Body is None.')
        else:
            return body