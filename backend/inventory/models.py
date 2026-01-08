from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from backend.products.models import Product

User = get_user_model()

class StockMovement(models.Model):
    MOVEMENT_TYPES = (
        ('in', 'Entrada'),
        ('out', 'Saída'),
        ('adjustment', 'Ajuste'),
        ('loss', 'Perda'),
        ('return', 'Devolução'),
    )

    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='stock_movements')
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_TYPES)
    quantity = models.IntegerField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # custo na hora da movimentação
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='stock_movements')
    reason = models.TextField(blank=True)
    reference = models.CharField(max_length=100, blank=True)  # pode ser número da nota, etc.
    expiration_date = models.DateField(null=True, blank=True)
    batch = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.unit_cost is not None:
            self.total_cost = self.unit_cost * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.movement_type} - {self.product.name} - {self.quantity}'

    class Meta:
        verbose_name = 'Movimentação de Estoque'
        verbose_name_plural = 'Movimentações de Estoque'

class InventoryAdjustment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='inventory_adjustments')
    previous_quantity = models.IntegerField()
    counted_quantity = models.IntegerField()
    adjustment = models.IntegerField()  # pode ser positivo ou negativo
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='inventory_adjustments')
    reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Ajuste de {self.product.name}'

    class Meta:
        verbose_name = 'Ajuste de Inventário'
        verbose_name_plural = 'Ajustes de Inventário'