from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

from .models import Profile


username_validator = UnicodeUsernameValidator()


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(max_length=15, min_length=2, required=True)
    last_name = forms.CharField(max_length=15, min_length=2, required=False)
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label=_("Password"), help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_("Confirm Password"))
    username = forms.CharField(label=_("Username"), max_length=30, min_length=3, required=True, help_text=_("30 characters or fewer. Letters, digits and @/./+/-/_ only."), validators=[username_validator], error_messages={"unique": _("Username already in use, please try a different one.")},)

    class Meta:
        model = Profile
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email", "type": "email"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password", "type": "password"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password", "type": "password"}),
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
        }


class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=15, min_length=2, required=True)
    last_name = forms.CharField(max_length=15, min_length=2, required=False)
    email = forms.EmailField(max_length=50, required=True)
    username = forms.CharField(label=_("Username"), max_length=30, help_text=_("30 characters or fewer. Letters, digits and @/./+/-/_ only."), validators=[username_validator], error_messages={"unique": _("Username already in use, please try a different one.")},)
    password = None

    class Meta:
        model = Profile
        fields = ("username", "first_name", "last_name", "email", "bio", "profile_pic")
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email", "type": "email"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password", "type": "password"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password", "type": "password"}),
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
            "bio": forms.Textarea(attrs={"class": "form-control", "placeholder": "Bio"}),
        }


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        required=True,
        label=_("Old Password"),
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Old Password",
                "type": "password",
            }
        ),
    )
    new_password1 = forms.CharField(
        required=True,
        label=_("Password"),
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "New Password",
                "type": "password",
            }
        ),
    )
    new_password2 = forms.CharField(
        required=True,
        label=_("Confirm Password"),
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm New Password",
                "type": "password",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")


# https://stackoverflow.com/questions/48049498/django-usercreationform-custom-fields
# https://www.youtube.com/watch?v=TBGRYkzXiTg&ab_channel=Codemy.com
