from django.conf.urls import url, include
from .views import home, admin
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    url(r'^login/$', login , {'template_name': 'CW/login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^$', home, name = 'home'),
    url(r'^admin_panel/$', admin, name = "admin")
]
