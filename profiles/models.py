from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user= self.create_user(email, password=password)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=15, blank=True, null=True)
    last_name = models.CharField(max_length=15, blank=True, null=True)
    about = models.TextField(max_length=500, blank=True) 
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")
    social_fb = models.CharField(max_length=100, null=True, blank=True)
    social_tw = models.CharField(max_length=100, null=True, blank=True)
    social_insta = models.CharField(max_length=100, null=True, blank=True)
    social_lin = models.CharField(max_length=100, null=True, blank=True)
    social_git = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin


    @property
    def is_active(self):
        return self.active


    # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # about = models.TextField(max_length=500, blank=True) 
    # profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")
    # social_fb = models.CharField(max_length=100, null=True, blank=True)
    # social_tw = models.CharField(max_length=100, null=True, blank=True)
    # social_insta = models.CharField(max_length=100, null=True, blank=True)
    # social_lin = models.CharField(max_length=100, null=True, blank=True)
    # social_git = models.CharField(max_length=100, null=True, blank=True)

    # def __str__(self):
    #     return str(self.user)