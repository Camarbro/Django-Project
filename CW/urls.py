from django.conf.urls import url, include
from .views import home, admin, RegisterMember, RegisterAssistant, RegisterStaff, RegisterConference, RegisterSpeaker
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    url(r'^login/$', login , {'template_name': 'CW/login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^$', home.as_view(), name = 'home'),
    url(r'^admin_panel/$', admin, name = "admin"),
    url(r'^register_member/$', RegisterMember.as_view() ,name = "registermemeber"),
    url(r'^register_assistant$', RegisterAssistant.as_view(), name = "registerassistant"),
    url(r'^register_staff$', RegisterStaff.as_view(), name = "registerstaff"),
    url(r'^register_conference$', RegisterConference.as_view() , name ="registerconference"),
    url(r'^register_speaker$', RegisterSpeaker.as_view() , name ="registerspeaker"),
]
