from unicodedata import name
from django.urls import URLPattern, path
from .views import AgemtsListView

app_name = 'agents'

urlpatterns = [
    path('', AgemtsListView.as_view(), name='agent-list'),
]