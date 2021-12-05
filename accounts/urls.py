from django.urls import path
from . import views

from .views import SignUpView, EditUserView, EditProfileView, ViewProfileView, ChangePasswordView, password_success

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<str:username>/edit_user/', EditUserView.as_view(), name='edit_user'),
    path('password/', ChangePasswordView.as_view(), name='change-password'),
    path('password_success/', views.password_success, name='password_success'),
    path('<str:username>/view_profile/', ViewProfileView.as_view(), name='view_profile'),
    path('<str:username>/edit_profile/', EditProfileView.as_view(), name='edit_profile')
]
