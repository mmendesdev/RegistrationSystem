import uuid

from django.db import models


class Businness(models.Model):
    Falseid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    social_name = models.CharField(max_length=500)  #
    is_active = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address_street = models.CharField(
        max_length=200, null=True, blank=True
    )  # endereço da empres
    andress_number = models.CharField(max_length=100, null=True, blank=True)
    andress_neighborhood = models.CharField(
        max_length=100, null=True, blank=True
    )  # bairro
    andress_city = models.CharField(max_length=100, null=True, blank=True)
    andress_state = models.CharField(max_length=2, null=True, blank=True)
    andress_zip_code = models.CharField(
        max_length=20, null=True, blank=True
    )  # campo de endereço
    description = models.TextField(null=True, blank=True)
    create_ate = models.DateTimeField(auto_now_add=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "businesses"

    def __str__(self):
        return self.social_name
