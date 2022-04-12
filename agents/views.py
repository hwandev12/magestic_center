from re import template
from django.views import generic
from django.urls import reverse
from .mixins import OrganiserAndLoginRequiredMixin
from base_app.models import Agent
from .forms import AgentModelForm

class AgentsListView(OrganiserAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/list.html'
    
    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Agent.objects.filter(organiser=organiser)
    
class AgentCreateView(OrganiserAndLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/create.html'
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse('agents:agent-list')
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organiser = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)
    
class AgentDetailView(OrganiserAndLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agents_detail.html'
    context_object_name = 'agent'
    
    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Agent.objects.filter(organiser=organiser)
    
class AgentUpdateView(OrganiserAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/update.html'
    form_class = AgentModelForm

    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Agent.objects.filter(organiser=organiser)
    
class AgentDeleteView(OrganiserAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/delete.html'
    context_object_name = 'agent'
    
    def get_success_url(self):
        return reverse('agents:agent-deleted')
    
    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Agent.objects.filter(organiser=organiser)
    
# Deleted agents flash
class AgentDeleted(OrganiserAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/deleted.html'
    queryset = Agent.objects.all()