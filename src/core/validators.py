
import re

from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

mobile_regex = r"^[6-9]\d{9}$"

mobile_validator = RegexValidator(
    re.compile(mobile_regex),
    message=_("Enter a valid 10 digit mobile number"),
    code="invalid",
)

pincode_regex = r"^[1-9][0-9]{5}$"

pincode_validator = RegexValidator(
    re.compile(pincode_regex),
    message=_("Enter a valid 6 digit pincode"),
    code="invalid",
)


class CustomPasswordValidator:
    """
    Validate whether the password is at least 8 characters long, contains minimum one uppercase and one lowercase.
    """
    def validate(self, password, user=None):
        if re.search('[A-Z]', password)==None or re.search('[a-z]', password)==None or len(password)<8:
            return False
        
        return True

    def get_help_text(self):
        return _("Your password must be at least 8 characters long, contain at least 1 uppercase and 1 lowercase character.")
