from django.db import models


class CPFField(models.CharField):
    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        print(value)
        return "".join([n for n in value if n.isdigit()])
