from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    CUSTOMER_TYPES = (
        ('individual', 'Pessoa Física'),
        ('company', 'Pessoa Jurídica'),
    )

    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPES, default='individual')
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    document = models.CharField(max_length=20, blank=True, verbose_name='CPF/CNPJ')
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'