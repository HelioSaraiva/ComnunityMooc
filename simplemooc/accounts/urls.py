from django.conf.urls import url, include
from django.contrib.auth import views
from simplemooc.accounts.views import register
from simplemooc.accounts.views import dashboard
from simplemooc.accounts.views import edit, edit_password, password_reset, password_reset_confirm
#from django.contrib import aut


urlpatterns = [
		url(r'^$', dashboard, name = 'dashboard'),
        url(r'^entrar/$', views.login, {'template_name': 'accounts/login.html'}, name = 'login'),
        url(r'^sair/$', views.logout, {'next_page': 'core:home'}, name = 'logout'),
        url(r'^confirmar-nova-senha/(?P<key>[\w]+)/$', password_reset_confirm, name = 'password_reset_confirm'),
        url(r'^cadastre-se/$', register, name = 'register'),
        url(r'^nova-senha/$', password_reset, name = 'password_reset'),
        url(r'^editar/$', edit, name = 'edit'),
        url(r'^editar-senha/$', edit_password, name = 'edit_password'),
        
]