from urllib.parse import urlencode

from django.views.generic import ListView

from market.models import Product, CATEGORIES


class IndexView(ListView):
    template_name = 'main.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['categories'] = CATEGORIES
        return context


