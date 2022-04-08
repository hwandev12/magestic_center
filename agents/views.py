from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from base_app.models import Agent

class AgemtsListView(LoginRequiredMixin, generic.ListView):
    template_name = 'agents/list.html'
    
    def get_queryset(self):
        return Agent.objects.all()
