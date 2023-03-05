from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=120)
    cpf = models.CharField(
        max_length=11,
        verbose_name="cpf",
        unique=True,
    )
    birth_date = models.DateField()

    class Meta:
        ordering = ["-id"]
