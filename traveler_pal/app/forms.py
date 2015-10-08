"""
created on 2015/10/8 at 21:36
"""
from django import forms

nameFieldMaxSize = 128


class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
    )
    password = forms.CharField(
        required=True,
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError("not valid")
        else:
            cleaned_data = super(LoginForm, self).clean()


class RegForm(forms.Form):
    username = forms.CharField(
        required=True,
        error_messages={'require': "shouldn't be null"},
    )
    email = forms.EmailField(
        required=True,
    )
    password = forms.CharField(
        required=True,
    )
