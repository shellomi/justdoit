from django import forms as django_forms
from django.contrib.auth import forms as auth_forms
from django.utils.translation import ugettext, ugettext_lazy as _


class CustomAuthenticaitonForm(auth_forms.AuthenticationForm):
    """docstring for CustomAuthenticaitonForm"""
    username = django_forms.CharField(max_length=254,
                                      widget=django_forms.TextInput(attrs={'required': '', 'autofocus': '', 'placeholder': 'Username',
                                                                           'class': 'form-control', 'id': 'inputUsername',
                                                                           'aria-describedby': 'username-addon'}))

    password = django_forms.CharField(label=_("Password"),
                                      widget=django_forms.PasswordInput(attrs={'required': '', 'placeholder': 'Password',
                                                                               'class': 'form-control', 'aria-describedby': 'pwd-addon',
                                                                               'id': 'inputPassword'}))

    # def __init__(self):
    #     super(CustomAuthenticaitonForm, self).__init__()
