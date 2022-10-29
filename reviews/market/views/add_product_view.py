from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from market.models import Product
from market.forms import AddEditProductForm
from market.views import CustomUserPassesMixin


class AddProductView(CustomUserPassesMixin, LoginRequiredMixin, CreateView):
    template_name = 'add_product.html'
    success_url = ('/')
    model = Product
    form_class = AddEditProductForm
    groups = ['moderator', 'root']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
