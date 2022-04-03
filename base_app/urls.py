from unicodedata import name
from django.urls import path
from .views import candidate_details, candidate, home

urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/', candidate_details),
    path('candidate/', candidate)
]
