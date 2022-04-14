from django.contrib import admin
from django.urls import path, include
from base_app.views import BaseView, SignupView
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView
)

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView.as_view(), name='home'),
    path('', include('base_app.urls', namespace='candidate')),
    path('agents/', include('agents.urls', namespace='agents')),
    path('login/', LoginView.as_view(), name='login'),
    path('password-reset-view/', PasswordResetView.as_view(), name='password_reset_view'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('register/', SignupView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout')
]
