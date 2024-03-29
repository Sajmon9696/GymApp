from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from accounts.forms import SignUpForm, UserProfileForm, MyLoginForm
from accounts.models import User


# Create your views here.

class MyLoginView(LoginView):
    """
        Widok logowania użytkownika.
        Używa niestandardowego formularza logowania i wyświetla niestandardowy szablon logowania.
        """
    form_class = MyLoginForm
    template_name = 'registration/login.html'


class SignUpView(CreateView):
    """
        Widok rejestracji nowego użytkownika.
        Umożliwia użytkownikowi rejestrację i automatyczne logowanie po pomyślnej rejestracji.
        """
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup_form.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:user_profile')


class TrainerSignUpView(CreateView):
    """
       Widok rejestracji nowego trenera.
       Umożliwia użytkownikowi rejestrację jako trener i automatyczne logowanie po pomyślnej rejestracji.
       """
    model = User
    form_class = SignUpForm
    template_name = 'registration/trainer_signup_form.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_trainer = True
        user.save()
        login(self.request, user)
        return redirect('accounts:user_profile')

def main_view(request):
    """
       Widok głównej strony.
       Wyświetla główną stronę witryny.
       """
    return render(request, template_name='main_site.html')


@login_required
def user_profile_view(request):
    """
        Widok profilu użytkownika.
        Wyświetla szczegóły profilu zalogowanego użytkownika.
        """
    user = request.user
    return render(request, 'user_profile.html', {'user': user})


@login_required
def update_user_profile_view(request):
    """
        Widok aktualizacji profilu użytkownika.
        Umożliwia użytkownikowi aktualizację swojego profilu.
        """
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:user_profile')
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'update_profile.html', {'form': form})
