from dataclasses import fields
from email.policy import default
from django import forms
from .models import Candidate

class MainRegister(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = (
            "name",
            "lastName",
            "email",
            "age",
            "job",
            "agent"
        )

# class RegisterForm(forms.Form):
#     name = forms.CharField(max_length=30)
#     lastName = forms.CharField(max_length=30)
#     age = forms.IntegerField()
#     email = forms.EmailField()
#     job = forms.CharField(max_length=30)