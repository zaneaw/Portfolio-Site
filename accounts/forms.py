from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.core.exceptions import FieldDoesNotExist
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator


username_validator = UnicodeUsernameValidator()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=15, min_length=2, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=15, min_length=2, required=True,
                               widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})))
    email = forms.EmailField(max_length=50, required=True,
                             widget=(forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email','type': 'email'})))
    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'type': 'password'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'type': 'password'}))
    username = forms.CharField(
        label=_('Username'),
        max_length=30,
        help_text=_('30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={'unique': _("Username already in use, please try a different one.")},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    # profile_pic = 

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=15, min_length=2, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=15, min_length=2, required=True,
                               widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})))
    email = forms.EmailField(max_length=50, required=True,
                             widget=(forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'email'})))
    username = forms.CharField(
        label=_('Username'),
        max_length=30,
        help_text=_('30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={'unique': _("Username already in use, please try a different one.")},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(required=True, label=_('Old Password'), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password', 'type': 'password'}))
    new_password1 = forms.CharField(required=True, label=_('Password'), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password', 'type': 'password'}))
    new_password2 = forms.CharField(required=True, label=_('Confirm Password'), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm New Password', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

# https://stackoverflow.com/questions/48049498/django-usercreationform-custom-fields
# https://www.youtube.com/watch?v=TBGRYkzXiTg&ab_channel=Codemy.com