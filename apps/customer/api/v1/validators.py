from textwrap import wrap
from datetime import datetime, date

from django.core.exceptions import ValidationError


def _calculate_verifier(digits, start=10):
    result = 0
    for digit in digits:
        result += start * int(digit)
        start -= 1
    mod = result % 11
    verifier = 0 if mod < 2 else 11 - mod
    return verifier


def cpf_validator(value):
    digits = wrap(value[:9], 1)
    first_verifier = _calculate_verifier(digits)
    digits.append(first_verifier)
    second_verifier = _calculate_verifier(digits, start=11)

    if first_verifier != int(value[9] or second_verifier != int(value[10])):
        raise ValidationError(
            "%(value)s is not a valid cpf.",
            params={"value": value},
        )


def birth_date_validator(date):
    if date > date.today():
        raise ValidationError(
            "Date %(date)s cannot be in the future.",
            params={"date": str(date)},
        )
