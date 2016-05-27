from django.conf.urls import url, include
from .views import home, admin, RegisterMember, RegisterAssistant, RegisterStaff, RegisterConference, RegisterSpeaker, ReportAssistants, ReportStaff, ReportMembers, ReportSpeakers, ReportConfereces
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
    url(r'^login/$', login , {'template_name': 'CW/login.html'}, name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
    url(r'^$', home.as_view(), name = 'home'),
    url(r'^admin_panel/$', admin, name = "admin"),
    url(r'^admin_panel/register_member/$', RegisterMember.as_view() ,name = "registermemeber"),
    url(r'^admin_panel/register_assistant$', RegisterAssistant.as_view(), name = "registerassistant"),
    url(r'^admin_panel/register_staff$', RegisterStaff.as_view(), name = "registerstaff"),
    url(r'^admin_panel/register_conference$', RegisterConference.as_view() , name ="registerconference"),
    url(r'^admin_panel/register_speaker$', RegisterSpeaker.as_view() , name ="registerspeaker"),
    url(r'^admin_panel/report_assistants/$', ReportAssistants.as_view(), name = "report_assistants"),
    url(r'^admin_panel/report_conferences/$', ReportConfereces.as_view(), name = "report_conferences"),
    url(r'^admin_panel/report_staff/$', ReportStaff.as_view(), name = "report_staff"),
    url(r'^admin_panel/report_members/$', ReportMembers.as_view(), name = "report_members"),
    url(r'^admin_panel/report_speakers/$', ReportSpeakers.as_view(), name = "report_speakers"),
]
