from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from market.forms import AddEditProductForm
from market.models import Review


class EditReviewView(LoginRequiredMixin, UpdateView):
    template_name = "edit_review.html"
    form_class = AddEditProductForm
    model = Review
    success_url = ('/')
    context_object_name = 'review'
    # groups = ['dev', 'lead', 'manager', 'root']
