from django.shortcuts import render
from .forms import AssistantForm, SpeakerForm, ConferenceForm, StaffForm, MembersForm
from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User, Permission
from .models import Assistant, Conference, Speaker, Members, Staff

# Create your views here.
class home(FormView):
    template_name = 'CW/home.html'
    form_class = AssistantForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        ctx = super(home, self).get_context_data(**kwargs)
        ctx['Conferences'] = Conference.objects.all()
        ctx['Speaker'] = Speaker.objects.all()
        return ctx

    def form_valid(self, form):
        p = Assistant()
        p.Name = form.cleaned_data['Name']
        p.Last_Name = form.cleaned_data['Last_Name']
        p.Age = form.cleaned_data['Age']
        p.email = form.cleaned_data['email']
        p.save()
        return super(home, self).form_valid(form)

def admin(request):
    return render(request, 'CW/admin.html')

class RegisterAssistant(FormView):
    template_name = 'CW/ra.html'
    form_class = AssistantForm
    success_url = reverse_lazy('admin')

    def form_valid(self,form):
        p = Assistant()
        p.Name = form.cleaned_data['Name']
        p.Last_Name = form.cleaned_data['Last_Name']
        p.Age = form.cleaned_data['Age']
        p.email = form.cleaned_data['email']
        p.save()
        return super(RegisterAssistant, self).form_valid(form)

class RegisterConference(FormView):
    template_name = 'CW/rc.html'
    form_class = ConferenceForm
    success_url = reverse_lazy('admin')

    def get_context_data(self, **kwargs):
        ctx = super(RegisterConference, self).get_context_data(**kwargs)
        ctx['Speaker'] = Speaker.objects.all()
        return ctx

    def form_valid(self,form):
        p = Conference()
        p.Title = form.cleaned_data['Title']
        p.Description = form.cleaned_data['Description']
        p.Speaker = form.cleaned_data['Speaker']
        p.Date = form.cleaned_data['Date']
        p.Time = form.cleaned_data['Time']
        p.Image = form.cleaned_data['Image']
        p.save()
        return super(RegisterConference, self).form_valid(form)

class RegisterStaff(FormView):
    template_name = 'CW/rs.html'
    form_class = StaffForm
    success_url = reverse_lazy('admin')

    def form_valid(self,form):
        p = Staff()
        p.Name = form.cleaned_data['Name']
        p.Task = form.cleaned_data['Task']
        p.Phone = form.cleaned_data['Phone']
        p.save()
        return super(RegisterStaff, self).form_valid(form)

class RegisterSpeaker(FormView):
    template_name = 'CW/rspkr.html'
    form_class = SpeakerForm
    success_url = reverse_lazy('admin')


    def form_valid(self,form):
        p = Speaker()
        p.Degree = form.cleaned_data['Degree']
        p.Name = form.cleaned_data['Name']
        p.Last_Name = form.cleaned_data['Last_Name']
        p.Picture = form.cleaned_data['Picture']
        p.save()
        return super(RegisterSpeaker, self).form_valid(form)

class RegisterMember(FormView):
    template_name = 'CW/rm.html'
    form_class = MembersForm
    success_url = reverse_lazy('admin')

    def form_valid(self,form):
        user = form.save()
        p = Members()
        p.User = user
        p.Name = user.first_name
        p.Last_Name = user.last_name
        p.Position = form.cleaned_data['Position']
        if p.Position == 'AD':
            perm = Permission.objects.get(codename = 'is_admin')
        elif p.Position == 'AC':
            perm = Permission.objects.get(codename = 'is_ac')
        elif p.Position == 'PC':
            perm = Permission.objects.get(codename = 'is_pc')
        elif p.Position == 'SC':
            perm = Permission.objects.get(codename = 'is_sc')
        p.User.user_permissions.add(perm)
        p.save()
        return super(RegisterMember, self).form_valid(form)
