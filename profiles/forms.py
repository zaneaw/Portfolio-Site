from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm, ReadOnlyPasswordHashField
from django.contrib.auth import password_validation, get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator


from .models import User, UserManager


username_validator = UnicodeUsernameValidator()
User = get_user_model()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=15, min_length=2, required=True)
    last_name = forms.CharField(max_length=15, min_length=2, required=False)
    email = forms.EmailField(max_length=30, required=True)
    password1 = forms.CharField(label=_('Password'), widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'type': 'password'})))
    password2 = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'type': 'password'}),
                                help_text=password_validation.password_validators_help_text_html())    
    # username = forms.CharField(label=_("Username"), max_length=12, min_length=2, required=True, help_text=_("30 characters or fewer. Letters, digits and @/./+/-/_ only."), validators=[username_validator], error_messages={"unique": _("Username already in use, please try a different one.")},)

    class Meta:
        model = User
        fields = (
            # "username",
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
            # "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
        }


class EditProfileForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields['about'].required = False

    first_name = forms.CharField(max_length=15, min_length=2, required=True)
    last_name = forms.CharField(max_length=15, min_length=2, required=False)
    email = forms.EmailField(max_length=50, required=True)
    # username = forms.CharField(label=_("Username"), max_length=30, help_text=_("30 characters or fewer. Letters, digits and @/./+/-/_ only."), validators=[username_validator], error_messages={"unique": _("Username already in use, please try a different one.")},)
    password = None

    class Meta:
        model = User
        fields = (
            # "username", 
            "first_name", 
            "last_name", 
            "email", 
            "about", 
            "social_fb", 
            "social_tw",
            "social_insta",
            "social_lin",
            "social_git",
            "profile_pic")
        labels = {
            "social_fb": "Facebook",
            "social_tw": "Twitter",
            "social_insta": "Instagram",
            "social_lin": "LinkedIn",
            "social_git": "GitHub",
        }
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email", "type": "email"}),
            # "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
            "about": forms.Textarea(attrs={"class": "form-control", "placeholder": "Describe yourself"}),
            "social_fb": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://facebook.com/user-name"}),
            "social_tw": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://twitter.com/user-name"}),
            "social_insta": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://instagram.com/user-name"}),
            "social_lin": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://linkedin.com/in/user-name"}),
            "social_git": forms.URLInput(attrs={"class": "form-control", "placeholder": "https://github.com/user-name"}),
        }


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(required=True, label=_("Old Password"))
    new_password1 = forms.CharField(required=True, label=_("Password"))
    new_password2 = forms.CharField(required=True, label=_("Confirm Password"))

    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")
        widgets = {
            'old_password': forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Old Password", "type": "password"}),
            'new_password1': forms.PasswordInput(attrs={"class": "form-control","placeholder": "New Password","type": "password",}),
            'new_password2': forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm New Password", "type": "password"}),
        }


# https://stackoverflow.com/questions/48049498/django-usercreationform-custom-fields
# https://www.youtube.com/watch?v=TBGRYkzXiTg&ab_channel=Codemy.com


class RegisterForm(forms.ModelForm):
    """
    The default 

    """

    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        '''
        Verify email is available.
        '''
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'password', 'active', 'admin']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]