from django.shortcuts import render
from .forms import AssistantForm
from django.views.generic import TemplateView, FormView, CreateView, ListView, UpdateView, DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User, Permission
from .models import Assistant, Conference, Speaker

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
