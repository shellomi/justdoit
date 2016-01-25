from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail


class Directory(models.Model):
    """docstring for Directory"""
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Category(models.Model):
    """docstring for Category"""
    name = models.CharField(max_length=50)
    directory = models.ForeignKey(Directory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    """docstring for Subcategory"""
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """docstring for Product"""
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image_name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class PatronManager(BaseUserManager):
    """docstring for PatronManager"""
    use_in_migrations = True

    def _create_user(self, first_name, last_name, company, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password and other user details.
        """
        if not email:
            raise ValueError('Email address must be set')
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, company=company, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, first_name, last_name, company, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(first_name, last_name, company, email, password, **extra_fields)

    def create_superuser(self, first_name, last_name, company, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(first_name, last_name, company, email, password, **extra_fields)


class Patron(AbstractBaseUser, PermissionsMixin):
    """docstring for Patron"""
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email address'), unique=True,
                              error_messages={
                              'unique': _("This email address is already in use"),
                              })
    company = models.CharField(_('company'), max_length=100)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = PatronManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'company']

    class Meta:
        verbose_name = _('patron')
        verbose_name_plural = _('patrons')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
