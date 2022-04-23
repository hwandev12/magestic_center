from django.shortcuts import redirect, render, reverse
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Candidate, Category
from django.views.generic import *
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


class Candidate_lists(LoginRequiredMixin, ListView):
    template_name = 'pages/candidates.html'
    context_object_name = 'candid'

    def get_queryset(self):
        user = self.request.user
        if user.is_organiser:
            queryset = Candidate.objects.filter(organiser=user.userprofile)
        else:
            queryset = Candidate.objects.filter(organiser=user.agent.organiser)
            queryset = queryset.filter(agent__user=self.request.user)
        return queryset

    # Bu yerda aniqlanmagan agent uchun funksiya yozilgan
    def get_context_data(self, **kwargs):  # Eslab qolish
        context = super(Candidate_lists, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organiser:
            queryset = Candidate.objects.filter(
                organiser=user.userprofile,
                agent__isnull=True
            )
            context.update({
                'unassigned_candidates': queryset
            })
            return context
    # Bu yerda aniqlanmagan agent uchun funksiya yozilgan


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


class AgentAssignView(OrganiserAndLoginRequiredMixin, FormView):
    template_name = 'pages/agent_find.html'
    form_class = AssignAgentForm

    # Bu qismda agentni tayinlash uchun yozilgan kwargs va qoshimchalar element
    def get_form_kwargs(self, **kwargs):
        kwargs = super(AgentAssignView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            'request': self.request
        })
        return kwargs

    def get_success_url(self):
        return reverse('candidate:candidate')

    def form_valid(self, form):
        agent = form.cleaned_data['agent']
        candidate = Candidate.objects.get(id=self.kwargs['pk'])
        candidate.agent = agent
        candidate.save()
        return super(AgentAssignView, self).form_valid(form)
    # Bu qismda agentni tayinlash uchun yozilgan kwargs va qoshimchalar element


class CategoryAssignView(LoginRequiredMixin, ListView):
    template_name = 'pages/category.html'
    context_object_name = 'candidates'

    def get_context_data(self, **kwargs):  # Eslab qolish
        context = super(CategoryAssignView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organiser:
            queryset = Candidate.objects.filter(
                organiser=user.userprofile
            )
        else:
            queryset = Category.objects.filter(
                organiser=user.agent.organiser)
        context.update({
            'unassigned_category_quantity': queryset.filter(category__isnull=True).count()
        })
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_organiser:
            queryset = Category.objects.filter(
                organiser=user.userprofile)
        else:
            queryset = Category.objects.filter(
                organiser=user.agent.organiser)
        return queryset


class AssignCategoryDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'details/category_detail.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_organiser:
            queryset = Category.objects.filter(
                organiser=user.userprofile)
        else:
            queryset = Category.objects.filter(
                organiser=user.agent.organiser)
        return queryset


# bu yerda category update qilish uchun yaratilgan
class CandidateCategoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'pages/category_update.html'
    form_class = LeadCategoryUpdateForm

    def get_queryset(self):
        user = self.request.user
        if user.is_organiser:
            queryset = Candidate.objects.filter(
                organiser=user.userprofile)
        else:
            queryset = Candidate.objects.filter(
                organiser=user.agent.organiser)
        return queryset

    def get_success_url(self):
        return reverse('candidate:candidate')
