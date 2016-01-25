from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views, forms

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^stationery/$', views.stationery, name='stationery'),
    url(r'^login/$', auth_views.login, {'template_name': 'ecommerce/registration/login.html',
                                        'authentication_form': forms.CustomAuthenticationForm}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'ecommerce/registration/password_reset.html'},
        name='password_reset'),
    url(r'^register/$', views.RegistrationView.as_view(), name='registration_register')
]
