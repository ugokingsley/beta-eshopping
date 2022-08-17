from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

 

class User(AbstractUser):
	full_name = models.CharField(max_length=140, blank=True, null=True)
	email = models.EmailField(unique=True, blank=True, default=None)

	#USERNAME_FIELD = 'email'
	#REQUIRED_FIELDS = ['username']

	def save(self, *args, **kwargs):
		super(User, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.email)

	@receiver(post_save, sender=settings.AUTH_USER_MODEL)
	def create_auth_token(sender, instance=None, created=False, **kwargs):
	    if created:
	        Token.objects.create(user=instance)

	class Meta:
		#pass
		ordering = ["-pk"]
