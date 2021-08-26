from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

from .models import Profile


username_validator = UnicodeUsernameValidator()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=15, min_length=2, required=True)
    last_name = forms.CharField(max_length=15, min_length=2, required=False)
    email = forms.EmailField(max_length=30, required=True)
    password1 = forms.CharField(label=_('Password'), widget=(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'type': 'password'})))
    password2 = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'type': 'password'}),
                                help_text=password_validation.password_validators_help_text_html())    
    username = forms.CharField(label=_("Username"), max_length=30, min_length=2, required=True, help_text=_("30 characters or fewer. Letters, digits and @/./+/-/_ only."), validators=[username_validator], error_messages={"unique": _("Username already in use, please try a different one.")},)

    class Meta:
        model = User
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
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
        }


class EditUserForm(UserChangeForm):
    first_name = forms.CharField(max_length=15, min_length=2, required=True)
    last_name = forms.CharField(max_length=15, min_length=2, required=False)
    email = forms.EmailField(max_length=50, required=True)
    username = forms.CharField(label=_("Username"), max_length=30, help_text=_("30 characters or fewer. Letters, digits and @/./+/-/_ only."), validators=[username_validator], error_messages={"unique": _("Username already in use, please try a different one.")},)
    password = None

    class Meta:
        model = User
        fields = (
            "username", 
            "first_name", 
            "last_name", 
            "email"
            )
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email", "type": "email"}),
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"}),
        }

class EditProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = Profile
        fields = ("about", "profile_pic", "facebook_url", "twitter_url", "instagram_url", "linkedin_url", "github_url")
        labels = {
            "facebook_url": "Facebook",
            "twitter_url": "Twitter",
            "instagram_url": "Instagram",
            "linkedin_url": "LinkedIn",
            "github_url": "GitHub",
        }
        widgets = {
            "about": forms.Textarea(attrs={"class": "form-control", "placeholder": "Dummy text? More like dummy thicc text, amirite? I'm baby bicycle rights poutine kale chips crucifix chartreuse leggings. Lo-fi mlkshk tousled, ramps PBR&B 8-bit gentrify keytar actually selvage kombucha cloud bread narwhal church-key sustainable. Pork belly put a bird on it blue bottle narwhal before they sold out authentic man braid. Edison bulb bitters artisan fam williamsburg kitsch. Biodiesel whatever marfa roof party raw denim artisan keffiyeh direct trade. Photo booth iPhone art party ennui. Irony sriracha small batch meggings, ennui kale chips paleo vinyl hot chicken authentic semiotics. Tousled trust fund hexagon everyday carry, scenester cardigan keytar +1 distillery four loko messenger bag etsy. Authentic jean shorts tote bag DIY whatever. Tumblr meggings small batch messenger bag fixie. Bitters listicle pour-over freegan hella lo-fi."}),
            "facebook_url": forms.TextInput(attrs={"class": "form-control", "placeholder": "https://facebook.com/user-name"}),
            "twitter_url": forms.TextInput(attrs={"class": "form-control", "placeholder": "https://twitter.com/user-name"}),
            "instagram_url": forms.TextInput(attrs={"class": "form-control", "placeholder": "https://instagram.com/user-name"}),
            "linkedin_url": forms.TextInput(attrs={"class": "form-control", "placeholder": "https://linkedin.com/in/user-name"}),
            "github_url": forms.TextInput(attrs={"class": "form-control", "placeholder": "https://github.com/user-name"}),
        }

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(required=True, label=_("Old Password"))
    new_password1 = forms.CharField(required=True, label=_("New Password"))
    new_password2 = forms.CharField(required=True, label=_("Confirm New Password"))

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
