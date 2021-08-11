from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=12, min_length=2, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=12, min_length=4, required=True,
                               widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})))
    email = forms.EmailField(max_length=50,
                             widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'})))
    password1 = forms.CharField(label=_('Password'),
                                widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})),
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label=_('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
                                help_text=_('Make sure the passwords match'))
    username = forms.CharField(
        label=_('Username'),
        max_length=30,
        help_text=_('30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={'unique': _("A user with that username already exists.")},
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


# https://stackoverflow.com/questions/48049498/django-usercreationform-custom-fields
# https://www.youtube.com/watch?v=TBGRYkzXiTg&ab_channel=Codemy.com