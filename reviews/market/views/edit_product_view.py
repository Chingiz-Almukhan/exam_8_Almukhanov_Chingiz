from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from market.forms import AddEditProductForm
from market.models import Product
from market.views import CustomUserPassesMixin


class EditProductView(CustomUserPassesMixin, LoginRequiredMixin, UpdateView):
    template_name = "edit_product.html"
    form_class = AddEditProductForm
    model = Product
    success_url = ('/')
    context_object_name = 'product'
    groups = ['moderator', 'root']
