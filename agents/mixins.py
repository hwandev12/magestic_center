from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin

class OrganiserAndLoginRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organiser:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

