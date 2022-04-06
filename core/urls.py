from django.contrib import admin
from django.urls import path, include
from base_app.views import BaseView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView.as_view(), name='home'),
    path('', include('base_app.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
