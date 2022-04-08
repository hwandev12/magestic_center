from django.contrib import admin
from .models import Candidate, Agent, User, UserProfile

admin.site.register(Candidate)
admin.site.register(UserProfile)
admin.site.register(Agent)
admin.site.register(User)

