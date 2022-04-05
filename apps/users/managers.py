#  interface for database with django models
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def email_validator(self, email):
        try:
            validate_email(email)
            valid_email = True
        except ValidationError:
            valid_email = False
            return False
        return valid_email
    def create_user(self, username, first_name, last_name, password, email, **extra_fields):
        if not username:
            raise ValueError(_('Users must submit a username'))
        if not first_name:
             raise ValueError(_('Users must submit a first name'))
        if not last_name:
             raise ValueError(_('Users must submit a last name'))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else: 
            raise ValueError(_('BAse User Account: an email is required'))

        user = self.model(
            username=username, first_name=first_name, last_name=last_name, email=email, **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Staff must have staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Super users must have staff=True"))
        if not password:
            raise ValueError(_("Super Users must have password"))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else: 
            raise ValueError(_('Admin Account: an email is required'))
        user = self.create_user(username, first_name, last_name, email, password, **extra_fields)
        user.save(using=self._db)
        return user
