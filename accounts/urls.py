from django.urls import path, include
from django.contrib.auth import views as auth_views

from accounts.views import main_view, SignUpView, user_profile_view, update_user_profile_view, MyLoginView

app_name = 'accounts'

urlpatterns = [
    path('', main_view, name='main'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/', SignUpView.as_view(), name='register_user'),
    path('profile/', user_profile_view, name='user_profile'),
    path('update_profile/', update_user_profile_view, name='update_user_profile'),

]
