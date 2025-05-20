from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

class UserIsOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != request.user:
            return redirect('/denied')
        return super().dispatch(request, *args, **kwargs)