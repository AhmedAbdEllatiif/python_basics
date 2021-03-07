from django.db import models
from datetime import datetime
from django.utils.translation import gettext as _


class Product(models.Model):
    
    class ProductRate(models.TextChoices):
        EXCELLENT = 5 , _('EXCELLENT')
        GREAT = 4, _('GREAT')
        GOOD = 3, _('GOOD')
        ACCEPTED = 2, _('ACCEPTED')
        POOR = 1,_('POOR')
        NOTRATED = 0,_('NOTRATED')
    
    title = models.CharField(max_length=40)
    description = models.TextField(default="")
    price = models.DecimalField(max_digits=19,decimal_places=2)
    rate = models.CharField(
        choices=ProductRate.choices,
        max_length=50,
        default= ProductRate.NOTRATED
        )
    created_at = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.title
    
    
    
