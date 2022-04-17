from dataclasses import fields
from email.policy import default
from urllib import request
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import Candidate, Agent

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

# Bu AssignaAgentForm da agenti yo'qni aniqlash va tayinlash uchun forma 
class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        agents = Agent.objects.filter(organiser=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields['agent'].queryset = agents
# Bu AssignaAgentForm da agenti yo'qni aniqlash va tayinlash uchun forma 