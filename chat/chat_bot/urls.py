from django.urls import path
from chat_bot.views import ChatView

urlpatterns = [
    path('', ChatView.as_view(),name="chat")
]