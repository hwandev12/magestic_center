from dataclasses import fields
from email.policy import default
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Candidate

User = get_user_model()

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

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}