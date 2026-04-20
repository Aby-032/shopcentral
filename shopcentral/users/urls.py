from django.urls import path
from .views import register_view, user_login, home_view, user_logout

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', user_login, name='login'),
    path('', home_view, name='home'),
    path('logout/', user_logout, name='logout'),
]