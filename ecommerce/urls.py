from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^stationery/$', views.stationery, name='stationery'),
    url(r'^login/$', auth_views.login, {'template_name': 'ecommerce/registration/login.html'}, name='login'),
    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'ecommerce/registration/password_reset.html'},
        name='password_reset')
]
