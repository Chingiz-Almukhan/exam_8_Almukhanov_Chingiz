from django.views.generic import DetailView

from market.models import Product, CATEGORIES


class ProductDetailView(DetailView):
    template_name = 'product_view.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        # task = IssueTracker.objects.filter(project=self.kwargs['pk'])
        context['categories'] = CATEGORIES
        return context
