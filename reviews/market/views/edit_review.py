from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic import UpdateView

from market.forms import AddEditProductForm
from market.models import Review
from market.views import CustomUserPassesMixin


class EditReviewView(PermissionRequiredMixin, UpdateView):
    template_name = "edit_review.html"
    form_class = AddEditProductForm
    model = Review
    success_url = ('/')
    context_object_name = 'review'
    permission_required = 'market.change_review'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user
