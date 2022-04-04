from multiprocessing import context
from django.shortcuts import redirect, render
from . import models
from .models import Candidate
from django.shortcuts import get_object_or_404
from .form import *


def home(request):
    return render(request, 'pages/main.html')


def candidate(request):
    candid = Candidate.objects.all()
    context = {"candid": candid}
    return render(request, 'pages/candidates.html', context)


def candidate_details(request, pk):
    candid = get_object_or_404(models.Candidate, id=pk)
    context = {"candid": candid}
    return render(request, 'details/candidate_details.html', context)


def register(request):
    form = MainRegister()
    if request.method == 'POST':
        form = MainRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"form": form}
    return render(request, 'pages/register.html', context)


def update_candidate(request, pk):
    candidate = models.Candidate.objects.get(id=pk)
    form = MainRegister(instance=candidate)
    if request.method == 'POST':
        form = MainRegister(request.POST, instance=candidate)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"candidate": candidate, "form": form}
    return render(request, 'pages/update.html', context)

def delete_candidate(request, pk):
    candidate = models.Candidate.objects.get(id=pk)
    candidate.delete()
    return redirect('/')