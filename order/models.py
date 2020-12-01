from django.db import models

from accounts.models import UserProfile
from product.models import Product


class Order(models.Model):
    items = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        items_count = self.items.all().count()
        return 'Order ({} items) by {}'.format(items_count, self.user)



