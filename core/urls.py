from django.contrib import admin
from django.urls import path, include
from base_app.views import BaseView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView.as_view(), name='home'),
    path('', include('base_app.urls'))
]
