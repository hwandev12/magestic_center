from unicodedata import name
from django.urls import path
from .views import *

app_name = 'candidate'

urlpatterns = [
    path('<int:pk>/', Candidate_details.as_view(), name='details'),
    path('<int:pk>/update/', Update_candidate.as_view(), name='update_info'),
    path('<int:pk>/delete/', Delete_candidate.as_view(), name='delete_info'),
    path('candidate/', Candidate_lists.as_view(), name='candidate'),
    path('signup/', Register.as_view(), name='register'),
    path('/deleted', Deleted.as_view(), name='deleted') 
]
