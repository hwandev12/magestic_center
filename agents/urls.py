from unicodedata import name
from django.urls import URLPattern, path
from .views import *

app_name = 'agents'

urlpatterns = [
    path('', AgentsListView.as_view(), name='agent-list'), 
    path('create-agents/', AgentCreateView.as_view(), name='agent-create'),
    path('delete-agents/', AgentDeleted.as_view(), name='agent-deleted'),
    path('<int:pk>/', AgentDetailView.as_view(), name='agent-details'),
    path('<int:pk>/update/', AgentUpdateView.as_view(), name='agent-update'),
    path('<int:pk>/delete/', AgentDeleteView.as_view(), name='agent-delete'),
]