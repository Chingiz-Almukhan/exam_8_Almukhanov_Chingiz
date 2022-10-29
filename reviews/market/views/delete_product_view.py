from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic import DeleteView

from market.models import Product


class DeleteProductView(LoginRequiredMixin, DeleteView):
    model = Product

    # groups = ['lead', 'manager', 'root']

    def get_success_url(self):
        return reverse_lazy('main')
