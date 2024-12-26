from django.urls import path
from .views import UserListCreateAPIView, MessageListCreateAPIView, ConversationListCreateAPIView

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user_list_create'),
    path('messages/', MessageListCreateAPIView.as_view(), name='message_list_create'),
    path('conversations/', ConversationListCreateAPIView.as_view(), name='conversation_list_create'),
]
