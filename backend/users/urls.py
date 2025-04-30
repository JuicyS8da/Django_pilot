from django.urls import path
from .views import login_view, register_view, sign_out

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', sign_out, name='logout')
]