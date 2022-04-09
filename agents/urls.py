from unicodedata import name
from django.urls import URLPattern, path
from .views import *

app_name = 'agents'

urlpatterns = [
    path('', AgentsListView.as_view(), name='agent-list'), 
    path('create-agents/', AgentCreateView.as_view(), name='agent-create'),
]