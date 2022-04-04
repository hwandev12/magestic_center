from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/', candidate_details),
    path('<int:pk>/update/', update_candidate),
    path('<int:pk>/delete/', delete_candidate),
    path('candidate/', candidate, name='candidate'),
    path('signup/', register, name='register')
]
