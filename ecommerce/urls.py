from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from . import views, forms

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^stationery/$', views.stationery, name='stationery'),
    url(r'^login/$', auth_views.login, {'template_name': 'ecommerce/registration/login.html',
                                        'authentication_form': forms.CustomAuthenticationForm}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'ecommerce/registration/password_reset.html'},
        name='password_reset'),
    url(r'^activate/complete/$',
        TemplateView.as_view(
            template_name='ecommerce/registration/activation_complete.html'
        ),
        name='registration_activation_complete'),
    url(r'^activate/(?P<activation_key>[-:\w]+)/$', views.ActivationView.as_view(), name='registration_activate'),
    url(r'^register/$', views.RegistrationView.as_view(), name='registration_register'),
    url(r'^register/complete/$',
        TemplateView.as_view(
            template_name='ecommerce/registration/registration_complete.html'
        ),
        name='registration_complete'),
    url(r'^register/closed/$',
        TemplateView.as_view(
            template_name='ecommerce/registration/registration_closed.html'
        ),
        name='registration_disallowed'),
]
