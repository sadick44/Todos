from django.urls import path
from .views import home, signup, todos, user_login


urlpatterns = [
    path('', home, name='home'),
    path('signup', signup, name="signup"),
    path('todos', todos, name="todos"),
    path('login', user_login, name="login")
]