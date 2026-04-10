from django.urls import path
from .view.main_view import home_view
from .view.auth_view import login_view,signup_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
]