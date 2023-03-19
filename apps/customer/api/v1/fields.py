from rest_framework.serializers import CharField

from apps.customer.api.v1.utils import clean_cpf


class CPFField(CharField):
    def to_internal_value(self, data):
        cleaned_data = clean_cpf(data)

        return super().to_internal_value(cleaned_data)
