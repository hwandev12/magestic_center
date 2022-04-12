from re import template
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from base_app.models import Agent
from .forms import AgentModelForm

class AgentsListView(LoginRequiredMixin, generic.ListView):
    template_name = 'agents/list.html'
    
    def get_queryset(self):
        profile = self.request.user.userprofile
        return Agent.objects.filter(profile=profile)
    
class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'agents/create.html'
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse('agents:agent-list')
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.profile = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)
    
class AgentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agents_detail.html'
    context_object_name = 'agent'
    
    def get_queryset(self):
        profile = self.request.user.userprofile
        return Agent.objects.filter(profile=profile)
    
class AgentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/update.html'
    form_class = AgentModelForm

    def get_queryset(self):
        profile = self.request.user.userprofile
        return Agent.objects.filter(profile=profile)
    
class AgentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/delete.html'
    context_object_name = 'agent'
    
    def get_success_url(self):
        return reverse('agents:agent-deleted')
    
    def get_queryset(self):
        profile = self.request.user.userprofile
        return Agent.objects.filter(profile=profile)
    
# Deleted agents flash
class AgentDeleted(LoginRequiredMixin, generic.ListView):
    template_name = 'agents/deleted.html'
    queryset = Agent.objects.all()