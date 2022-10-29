from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from market.models import Review


def delete(LoginRequiredMixin, request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('main')
