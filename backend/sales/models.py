from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from backend.products.models import Product
from backend.customers.models import Customer

User = get_user_model()

class Sale(models.Model):
    SALE_STATUS = (
        ('pending', 'Pendente'),
        ('completed', 'Concluída'),
        ('canceled', 'Cancelada'),
        ('refunded', 'Estornada'),
    )

    sale_number = models.CharField(max_length=20, unique=True, verbose_name='Número da Venda')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='sales')
    operator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sales')
    status = models.CharField(max_length=20, choices=SALE_STATUS, default='pending')
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sale_number} - {self.customer.name if self.customer else "Sem cliente"}'

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='sale_items')
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calcula o total do item
        self.total = (self.unit_price * self.quantity) - self.discount_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} x {self.quantity}'

    class Meta:
        verbose_name = 'Item de Venda'
        verbose_name_plural = 'Itens de Venda'

class Payment(models.Model):
    PAYMENT_METHODS = (
        ('cash', 'Dinheiro'),
        ('credit_card', 'Cartão de Crédito'),
        ('debit_card', 'Cartão de Débito'),
        ('pix', 'PIX'),
        ('transfer', 'Transferência'),
        ('other', 'Outro'),
    )

    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='payments')
    method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=100, blank=True)  # número do cartão, código PIX, etc.
    status = models.CharField(max_length=20, default='completed')  # pending, completed, failed
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.method} - {self.amount}'

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'