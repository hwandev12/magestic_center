from unicodedata import name
from django.urls import path
from .views import *

app_name = 'candidate'

urlpatterns = [
    path('<int:pk>/', Candidate_details.as_view(), name='details'),
    path('<int:pk>/update/', Update_candidate.as_view(), name='update'),
    path('<int:pk>/delete/', Delete_candidate.as_view(), name='delete'),
    path('<int:pk>/assign-agent/', AgentAssignView.as_view(), name='assign_agent'),
    path('<int:pk>/category-update-detail/',
         CandidateCategoryUpdateView.as_view(), name='category_update_detail'),
    path('candidate/', Candidate_lists.as_view(), name='candidate'),
    path('create/', Candidate_create.as_view(), name='create'),
    path('deleted/', Deleted.as_view(), name='deleted'),
    path('category-lists/', CategoryAssignView.as_view(), name='category'),
    path('category-lists/<int:pk>/',
         AssignCategoryDetailsView.as_view(), name='category_detail'),
]
