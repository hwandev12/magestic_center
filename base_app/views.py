from multiprocessing import context
from django.shortcuts import redirect, render
from . import models
from .models import Candidate
from django.shortcuts import get_object_or_404
from .form import RegisterForm


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
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            lastName = form.cleaned_data['lastName']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            job = form.cleaned_data['job']
            agent = models.Agent.objects.first()
            models.Candidate.objects.create(name=name,
                                            lastName=lastName,
                                            age=age,
                                            email=email,
                                            job=job,
                                            agent=agent)
            return redirect('/')
    context = {"form": form}
    return render(request, 'pages/register.html', context)

def update_candidate(request, pk):
    candidate = Candidate.objects.get(id=pk)
    context = {
        "candidate": candidate
    }
    return render(request, 'pages/update.html', context)