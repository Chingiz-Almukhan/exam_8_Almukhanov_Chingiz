from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from accounts.forms import LoginForm, MyUserCreationForm
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView


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


