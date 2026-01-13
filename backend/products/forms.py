from django import forms  # Apenas esta importação de django é necessária aqui
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'sku', 'barcode', 'name', 'category', 
            'unit_cost', 'sale_price', 'minimum_stock', 
            'current_stock', 'description', 'is_active'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }