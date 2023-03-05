from rest_framework.serializers import ModelSerializer, CharField, DateField
from rest_framework.validators import UniqueValidator

from apps.customer.models import Customer
from apps.customer.api.v1.validators import cpf_validator, birth_date_validator
from apps.customer.api.v1.utils import clean_cpf


class CustomerSerializer(ModelSerializer):
    cpf = CharField(
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

    def to_internal_value(self, data):
        if "cpf" in data.keys():
            data._mutable = True
            data["cpf"] = clean_cpf(data["cpf"])

        return super(CustomerSerializer, self).to_internal_value(data)
