from django.contrib.auth.mixins import AccessMixin
from django.views.generic import TemplateView

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'home.html'


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done'


class OwnerOnlyMixin(AccessMixin): # 주인만 지울 수 있게 하는
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the objectj"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
