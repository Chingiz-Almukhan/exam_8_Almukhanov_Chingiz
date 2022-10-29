from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from market.models import Product
from market.forms import AddEditProductForm


class AddProductView(LoginRequiredMixin, CreateView):
    template_name = 'add_product.html'
    success_url = ('/')
    model = Product
    form_class = AddEditProductForm

    # groups = ['manager', 'root']

    # def get_success_url(self):
    #     set_user = get_object_or_404(Product, pk=self.object.pk)
    #     set_user.users.add(self.request.user)
    #     set_user.save()
    #     return redirect('projects')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
