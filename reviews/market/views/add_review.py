from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView

from market.models import Review, Product
from market.forms import AddEditReviewForm


class AddReviewView(LoginRequiredMixin, CreateView):
    template_name = 'add_review.html'
    model = Review
    form_class = AddEditReviewForm
    # groups = ['manager', 'root']

    def get_success_url(self):
        return redirect('main')

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.author = self.request.user
        review.save()
        return redirect('product_detail', pk=product.pk)


