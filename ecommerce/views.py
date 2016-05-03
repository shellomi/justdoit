from django.shortcuts import render
from django.views.generic import UpdateView
from oscar.apps.customer.forms import ProfileForm, PasswordChangeForm, ConfirmPasswordForm
from registration.backends.hmac.views import RegistrationView as BaseRegistrationView, ActivationView as BaseActivationView
from . import models, forms


def home(request):
    return render(request, 'ecommerce/index.html')


def stationery(request):
    directories = models.Directory.objects.all()
    categories = models.Category.objects.all()
    subcategories = models.Subcategory.objects.all()
    products = models.Product.objects.all()
    dirs = []
    for directory in directories:
        dirt = Dir(directory.pk, directory.name)
        for category in categories:
            if category.directory_id != directory.pk:
                continue
            cat = Cat(category.name)
            for subcategory in subcategories:
                if category.pk != subcategory.category_id:
                    continue
                sub = Sub(subcategory.name)
                cat.subcategories.append(sub)
            dirt.categories.append(cat)
        dirs.append(dirt)
    return render(request, 'ecommerce/stationery.html',
                  {'directories': dirs,
                   'products': products})


# def login(request):
#     template_response = auth_views.login()


class Dir:
    """docstring for Dir"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.categories = []

    def __str__(self):
        return self.name


class Cat:
    """docstring for Cat"""
    def __init__(self, name):
        self.name = name
        self.subcategories = []

    def __str__(self):
        return self.name


class Sub:
    """docstring for Sub"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class RegistrationView(BaseRegistrationView):
    """docstring for RegistrationView"""
    form_class = forms.RegistrationForm
    template_name = 'ecommerce/registration/registration_form.html'
    email_body_template = 'ecommerce/registration/activation_email.txt'
    email_subject_template = 'ecommerce/registration/activation_email_subject.txt'


class ActivationView(BaseActivationView):
    """docstring for ActivationView"""
    template_name = 'ecommerce/registration/activate.html'

class ProfileView(UpdateView):
    template_name = 'ecommerce/partials/profile.html'
    profile_form_class = ProfileForm
    passwordchange_form_class = PasswordChangeForm
