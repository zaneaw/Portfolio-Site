from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),
    path('password/', ChangePasswordView.as_view(), name='change-password'),
    path('password_success/', password_success, name='password_success'),
    path('<int:pk>/view_profile/', ViewProfileView.as_view(), name='view_profile'),
]