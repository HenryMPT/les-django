from django.utils.translation import ngettext  # https://docs.python.org/2/library/gettext.html#gettext.ngettext
from django.core.exceptions import ValidationError

class MyCustomMinimumLengthValidator(object):
        def __init__(self, min_length=8):  # put default min_length here
            self.min_length = min_length

        def validate(self, password, user=None):
            if len(password) < self.min_length:
                raise ValidationError(
                    ngettext(
                        # silly, I know, but if your min length is one, put your message here
                        "This password is too poopie. It must contain at least %(min_length)d character.",
                        # if it's more than one (which it probably is) put your message here
                        "This password is too poopie.. It must contain at least %(min_length)d characters.",
                        self.min_length
                    ),
                code='password_too_short',
                params={'min_length': self.min_length},
                )

        def get_help_text(self):
            return ngettext(
                # you can also change the help text to whatever you want for use in the templates (password.help_text)
                "Your password must contain at three poops least %(min_length)d character.",
                "Your password must contain at ppoos least %(min_length)d characters.",
                self.min_length
            ) % {'min_length': self.min_length}