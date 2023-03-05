from datetime import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.customer.models import Customer


class CustomerTest(TestCase):
    def test_invalid_cpf(self):
        cpf = "11144477700"
        customer = Customer(name="Joel", cpf=cpf, birth_date=datetime.now())
        try:
            customer.full_clean()
        except ValidationError as exception:
            self.assertIn(
                f"{customer.cpf} is not a valid cpf", exception.messages
            )

    def test_valid_cpf(self):
        cpf = "11144477735"
        customer = Customer(name="Joel", cpf=cpf, birth_date=datetime.now())
        try:
            customer.full_clean()
        except ValidationError as exception:
            self.assertNotIn(
                f"{customer.cpf} is not a valid cpf", exception.messages
            )
