import math

from django.views.generic import DetailView

from market.forms import AddEditReviewForm
from market.models import Product, CATEGORIES, Review


class ProductDetailView(DetailView):
    template_name = 'product_view.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['review'] = Review.objects.filter(product=self.kwargs['pk'])
        raiting = []
        all_rait = 0
        for i in context['review']:
            raiting.append(i.grade)
        for i in raiting:
            all_rait += int(i)
        context_raiting = all_rait / len(raiting)
        context['raiting'] = math.ceil(context_raiting)
        context['categories'] = CATEGORIES
        return context
