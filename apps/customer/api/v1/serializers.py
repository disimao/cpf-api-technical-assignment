from rest_framework.serializers import ModelSerializer, CharField, DateField
from rest_framework.validators import UniqueValidator

from apps.customer.models import Customer
from apps.customer.api.v1.validators import cpf_validator, birth_date_validator
from apps.customer.api.v1.fields import CPFField


class CustomerSerializer(ModelSerializer):
    cpf = CPFField(
        validators=[
            UniqueValidator(queryset=Customer.objects.all()),
            cpf_validator,
        ]
    )
    birth_date = DateField(
        validators=[
            birth_date_validator,
        ]
    )

    class Meta:
        model = Customer
        fields = ["name", "cpf", "birth_date"]
