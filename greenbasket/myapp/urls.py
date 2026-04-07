from django.urls import path
from .view.main_view import home_view

urlpatterns = [
    path('', home_view, name='home')
]