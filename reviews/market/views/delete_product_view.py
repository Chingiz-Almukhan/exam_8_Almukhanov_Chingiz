from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.views.generic import DeleteView

from market.models import Product
from market.views import CustomUserPassesMixin


class DeleteProductView(CustomUserPassesMixin, LoginRequiredMixin, DeleteView):
    model = Product
    groups = ['moderator', 'root']

    def get_success_url(self):
        return reverse_lazy('main')
