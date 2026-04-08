from django.urls import path
from .views import register_view, user_login, user_logout

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]