from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from django import forms

from accounts.models import User, Trainer

INPUT_CLASSES = 'form-control'


class MyLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password'}))


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Repeat Password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        widgets = {

            'username': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Username',
            }),
            'first_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Last Name',
            }),
            'email': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'E-mail',
            }),

        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        if user.is_trainer:
            Trainer.objects.create(user=user)
        return user


class UserProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['gender', 'height_cm', 'weight_kg', 'squat_record_kg', 'dead_lift_record_kg', 'bench_press_record_kg',
                  'pull_up_record_amount', 'dips_record_amount']

        widgets = {

            'gender': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
            'height_cm': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'weight_kg': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'squat_record_kg': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'dead_lift_record_kg': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'bench_press_record_kg': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'pull_up_record_amount': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
            'dips_record_amount': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
            }),
        }
