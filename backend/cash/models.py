from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class CashSession(models.Model):
    SESSION_STATUS = (
        ('open', 'Aberto'),
        ('closed', 'Fechado'),
    )

    operator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='cash_sessions')
    opening_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Saldo Inicial')
    closing_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Saldo Final')
    status = models.CharField(max_length=20, choices=SESSION_STATUS, default='open')
    opened_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    sales = models.ManyToManyField('sales.Sale', related_name='cash_sessions', blank=True)

    def __str__(self):
        return f'Sessão de {self.operator.username} - {self.opened_at}'

    class Meta:
        verbose_name = 'Sessão de Caixa'
        verbose_name_plural = 'Sessões de Caixa'

class CashMovement(models.Model):
    MOVEMENT_TYPES = (
        ('income', 'Entrada'),
        ('outcome', 'Saída'),
    )

    session = models.ForeignKey(CashSession, on_delete=models.CASCADE, related_name='movements')
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movement_type} - {self.amount}'

    class Meta:
        verbose_name = 'Movimentação de Caixa'
        verbose_name_plural = 'Movimentações de Caixa'