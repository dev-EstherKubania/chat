from django.urls import path, include
from chat import views as chat_views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path("", chat_views.chatPage, name="chat-page"),
    # login-section
    path('chat_view/', views.chat_view, name='chat_view'),
    path("auth/login/", LoginView.as_view(template_name="chat/LoginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(template_name="chat/LogOut.html"), name="logout-user"),
]