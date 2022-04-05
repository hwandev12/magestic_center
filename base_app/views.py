from multiprocessing import context
from re import template
from django.shortcuts import redirect, render, reverse
from . import models
from .models import Candidate
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .form import *


class BaseView(TemplateView):
    template_name = 'pages/main.html'
    
    
class Candidate_lists(ListView):
    template_name = 'pages/candidates.html'
    queryset = Candidate.objects.all()
    context_object_name = 'candid'
    
class Candidate_details(DetailView):
    template_name = 'details/candidate_details.html'
    queryset = Candidate.objects.all()
    context_object_name = 'candid'
    
class Register(CreateView):
    template_name = 'pages/register.html'
    form_class = MainRegister
    
    def get_success_url(self):
        return reverse('candidate:candidate')
    
class Update_candidate(UpdateView):
    template_name = 'pages/update.html'
    form_class = MainRegister
    queryset = models.Candidate.objects.all()
    context_object_name = 'candidate'
    
    def get_success_url(self):
        return reverse('candidate:candidate')

class Delete_candidate(DeleteView):
    template_name = 'pages/candidate_confirm_delete.html'
    form_class = MainRegister
    queryset = models.Candidate.objects.all()
    
    def get_success_url(self): 
        return reverse('candidate:deleted')
    
class Deleted(ListView):
    template_name = 'pages/deleted.html'
    queryset = models.Candidate.objects.all()
