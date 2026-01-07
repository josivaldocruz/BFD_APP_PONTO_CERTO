from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True, verbose_name='SKU')
    barcode = models.CharField(max_length=100, blank=True, verbose_name='Código de Barras')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Custo Unitário')
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço de Venda')
    minimum_stock = models.IntegerField(default=0, verbose_name='Estoque Mínimo')
    current_stock = models.IntegerField(default=0, verbose_name='Estoque Atual')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.sku})'

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'