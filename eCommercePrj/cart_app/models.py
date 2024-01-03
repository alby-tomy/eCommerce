from django.db import models

# Create your models here.
from e_commerceApp.models import Product


class Cart(models.Model):
    cart_id = models.CharField(max_length=280, blank=True)
    date_added = models.DateField(auto_now_add = True)
    
    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']
        
    def __str__(self):
        return '{}'.format(self.cart_id)
    
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'CartItem'
        
    def subTotal(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return '{}'.format(self.product)