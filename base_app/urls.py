from unicodedata import name
from django.urls import path
from .views import *

app_name = 'candidate'

urlpatterns = [
    path('<int:pk>/', Candidate_details.as_view(), name='details'),
    path('<int:pk>/update/', Update_candidate.as_view(), name='update'),
    path('<int:pk>/delete/', Delete_candidate.as_view(), name='delete'),
    path('candidate/', Candidate_lists.as_view(), name='candidate'),
    path('signup/', Register.as_view(), name='create'),
    path('/deleted', Deleted.as_view(), name='deleted') 
]
