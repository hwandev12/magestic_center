from multiprocessing import context
from django.shortcuts import render
from . import models
from .models import Candidate
from django.shortcuts import get_object_or_404


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
