from django.urls import path
from . import views

from .views import SignUpView, EditUserView, ChangePasswordView, ViewProfileView, password_success

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit_user/', EditUserView.as_view(), name='edit_user'),
    path('password/', ChangePasswordView.as_view(), name='change-password'),
    path('password_success/', password_success, name='password_success'),
    path('<int:pk>/view_profile/', ViewProfileView.as_view(), name='view_profile'),
]