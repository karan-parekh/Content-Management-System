from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

from .managers import UserManager
from .validators import mobile_validator, pincode_validator


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=128)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    phone = models.CharField(
        max_length=10,
        validators=[mobile_validator],
        unique=True,
    )
    address = models.TextField(blank=True, null=True)
    city    = models.CharField(max_length=64, blank=True, null=True)
    state   = models.CharField(max_length=64, blank=True, null=True)
    country = models.CharField(max_length=64, blank=True, null=True)
    pincode = models.CharField(
        max_length=6,
        validators = [pincode_validator]
    )
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    REQUIRED_FIELDS = ['full_name', 'phone', 'pincode'] # Email & Password are required by default.
    USERNAME_FIELD = "email"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin


class Content(models.Model):

    CATEGORIES = (
        ("BOND", _("BOND")),
        ("CERTIFICATE", _("CERTIFICATE")),
        ("LICENSE", _("LICENSE")),
        ("PASSPORT", _("PASSPORT")),
        ("CONTRACT", _("CONTRACT")),
    )

    author   = models.ForeignKey(User, related_name="contents", on_delete=models.PROTECT)
    title    = models.CharField(max_length=30, blank=False)
    body     = models.TextField(max_length=300, blank=False)
    summary  = models.TextField(max_length=60, blank=False)
    document = models.FileField(upload_to="media", null=False, blank=False, validators=[FileExtensionValidator(
        allowed_extensions=["pdf"], message=_("Uploaded document is not a pdf"), code="invalid_file_format"
    )])
    categories = MultiSelectField(choices=CATEGORIES)
