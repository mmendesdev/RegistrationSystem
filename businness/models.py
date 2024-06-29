import uuid
from django.db import models
# modelando a tabela do projeto
#preciso dá um comando = python manage.py makemigrations para tranformar minha class em sql
#logo depois um = python manage.py migrate , para pegr pegar as migrations e apliar no banco de dados

class Business(models.Model):
    Falseid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    social_name = models.CharField(max_length=500) #nome da empresa
    cnpj = models.CharField(max_length=14)
    is_active = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, null=True, blank=True) #telefone
    address_street = models.CharField(max_length=200, null=True, blank=True) #endereço da empres
    andress_number = models.CharField(max_length=100, null=True, blank=True)
    andress_neighborhood = models.CharField(max_length=100, null=True, blank=True) #bairro
    andress_city = models.CharField(max_length=100, null=True, blank=True) #cidade
    andress_state = models.CharField(max_length=2, null=True, blank=True) #estado
    andress_zip_code = models.CharField(max_length=20, null=True, blank=True) #campo de endereço
    description = models.TextField(null=True, blank=True) #descreção da empresa
    create_ate = models.DateTimeField(auto_now_add=True) # Que horas a empresa foi cadastrada
    create_at = models .DateTimeField(auto_now_add=True) # 

   #colando no plural para não dar bug 
    class Meta:
        verbose_name_plural = 'businesses'

    def __str__(self):
        return self.social_name
    