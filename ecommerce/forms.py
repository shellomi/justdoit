from django import forms as django_forms
from django.contrib.auth import forms as auth_forms
from django.utils.translation import ugettext_lazy as _
from .models import Patron
from registration.forms import RegistrationForm as BaseRegistrationForm


class CustomAuthenticationForm(auth_forms.AuthenticationForm):
    """docstring for CustomAuthenticationForm"""
    email = django_forms.EmailField(widget=django_forms.EmailInput(attrs={'required': '', 'autofocus': '', 'placeholder': 'Email',
                                                                          'class': 'form-control',
                                                                          'aria-describedby': 'email-addon'}))

    password = django_forms.CharField(label=_("Password"),
                                      widget=django_forms.PasswordInput(attrs={'required': '', 'placeholder': 'Password',
                                                                               'class': 'form-control', 'aria-describedby': 'pwd-addon'}))

    # def __init__(self):
    #     super(CustomAuthenticationForm, self).__init__()


class RegistrationForm(BaseRegistrationForm):
    """
    Form for registering a new user account.
    Validates that the requested username is not already in use, and
    requires the password to be entered twice to catch typos.
    Subclasses should feel free to add any additional validation they
    need, but should take care when overriding ``save()`` to respect
    the ``commit=False`` argument, as several registration workflows
    will make use of it to create inactive user accounts.
    """
    first_name = django_forms.CharField(label=_("First name"), max_length=30)
    last_name = django_forms.CharField(label=_("Last name"), max_length=30)
    company = django_forms.CharField(label=_("Company"), max_length=100)

    email = django_forms.EmailField(widget=django_forms.EmailInput(attrs={'required': '', 'autofocus': '', 'placeholder': 'Email',
                                                                          'class': 'form-control',
                                                                          'aria-describedby': 'email-addon'}))

    password1 = django_forms.CharField(label=_("Password"),
                                       widget=django_forms.PasswordInput(attrs={'required': '', 'placeholder': 'Password',
                                                                                'class': 'form-control', 'aria-describedby': 'pwd-addon'}))
    password2 = django_forms.CharField(label=_("Password confirmation"),
                                       widget=django_forms.PasswordInput(attrs={'required': '', 'placeholder': 'Password',
                                                                                'class': 'form-control', 'aria-describedby': 'pwd-addon'}),
                                       help_text=_("Enter the same password as before, for verification."))

    class Meta(BaseRegistrationForm.Meta):
        model = Patron
        fields = [
            'first_name',
            'last_name',
            'company',
            'email',
            'password1',
            'password2',
        ]
