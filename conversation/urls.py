from django.urls import path
from django.contrib.auth import views as auth_views
from .views import NewMessageView, InboxView, ConversationDetail

app_name = 'conversation'

urlpatterns = [
    path('new_message/', NewMessageView.as_view(), name='new_message'),
    path('inbox/', InboxView.as_view(), name='inbox'),
    path('detail/<int:pk>', ConversationDetail.as_view(), name='detail'),


]