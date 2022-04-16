from multiprocessing import context
from re import template
from django.shortcuts import redirect, render, reverse
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Candidate
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .form import *
from agents.mixins import OrganiserAndLoginRequiredMixin



class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = NewUserForm
    
    def get_success_url(self):
        return reverse('candidate:candidate')

class BaseView(TemplateView):
    template_name = 'pages/main.html'
    
    
class Candidate_lists(LoginRequiredMixin ,ListView):
    template_name = 'pages/candidates.html'
    context_object_name = 'candid' 
    def get_queryset(self):
        user = self.request.user
        if user.is_organiser:
            queryset = Candidate.objects.filter(organiser = user.userprofile)
        else:
            queryset = Candidate.objects.filter(organiser = user.agent.organiser)
            queryset = queryset.filter(agent__user = self.request.user)
        return queryset
    
class Candidate_details(OrganiserAndLoginRequiredMixin, DetailView):
    template_name = 'details/candidate_details.html'
    queryset = Candidate.objects.all()
    context_object_name = 'candid'
    
class Candidate_create(LoginRequiredMixin, CreateView):
    template_name = 'pages/candid_create.html'
    form_class = MainRegister
    
    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.organiser = self.request.user.userprofile
        lead.save()
        return super(Candidate_create, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('candidate:candidate')
    
class Update_candidate(OrganiserAndLoginRequiredMixin, UpdateView):
    template_name = 'pages/update.html'
    form_class = MainRegister
    queryset = models.Candidate.objects.all()
    context_object_name = 'candidate'
    
    def get_success_url(self):
        return reverse('candidate:candidate')

class Delete_candidate(OrganiserAndLoginRequiredMixin, DeleteView):
    template_name = 'pages/candidate_confirm_delete.html'
    queryset = models.Candidate.objects.all()
    
    def get_success_url(self): 
        return reverse('candidate:deleted')
    
class Deleted(OrganiserAndLoginRequiredMixin, ListView):
    template_name = 'pages/deleted.html'
    queryset = models.Candidate.objects.all()
