from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse

from accounts.forms import LoginForm, MyUserCreationForm, UserChangeForm, PasswordChangeForm
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView

from market.models import Review


class LoginView(TemplateView):
    form = LoginForm
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect('login')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username,
                            password=password)
        if not user:
            return redirect('login')
        login(request, user)
        return redirect('main')


def logout_view(request):
    logout(request)
    return redirect('main')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = MyUserCreationForm
    success_url = 'main'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
        context = {}
        context['form'] = form
        return self.render_to_response(context)


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        reviews = Review.objects.filter(author=self.request.user)
        context['reviews'] = reviews
        return context


class UserChangeView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = 'user_change.html'
    context_object_name = 'user_obj'


class UserPasswordChangeView(UpdateView):
    model = get_user_model()
    template_name = 'user_password_change.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('accounts:login')
