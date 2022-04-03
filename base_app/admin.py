from django.contrib import admin
from .models import Candidate, Agent, User

admin.site.register(Candidate)
admin.site.register(Agent)
admin.site.register(User)

