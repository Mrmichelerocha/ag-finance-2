from django.db import models
from django.utils import timezone
from django.http import JsonResponse

class Analyse(models.Model):
    ORDER_CHOICES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    ]
    STATUS_CHOICES = [
        ('on', 'On'),
        ('off', 'Off'),
    ]

    symbol = models.CharField(max_length=10)
    order = models.CharField(max_length=4, choices=ORDER_CHOICES)
    quantity = models.IntegerField()
    price_now = models.FloatField()
    minimum = models.FloatField()
    maximum = models.FloatField()
    direction = models.DecimalField(max_digits=10, decimal_places=2)
    metric = models.IntegerField()
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='on')
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.order == 'buy' and self.status == 'on':
            Buy.objects.create(symbol=self.symbol, price=self.price_now, order=self.order, quantity=self.quantity, status='on')
        elif self.order == 'sell' and self.status == 'on':
            Sell.objects.create(symbol=self.symbol, price=self.price_now, order=self.order, quantity=self.quantity, status='on')
        super().save(*args, **kwargs)
        
class Buy(models.Model):
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.CharField(max_length=4, choices=Analyse.ORDER_CHOICES)
    quantity = models.IntegerField()
    status = models.CharField(max_length=3, choices=Analyse.STATUS_CHOICES, default='on')
    date = models.DateTimeField(auto_now_add=True)

class Sell(models.Model):
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.CharField(max_length=4, choices=Analyse.ORDER_CHOICES)
    quantity = models.IntegerField()
    status = models.CharField(max_length=3, choices=Analyse.STATUS_CHOICES, default='on')
    date = models.DateTimeField(auto_now_add=True)

class Wallet(models.Model):
    symbol = models.CharField(max_length=10)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.CharField(max_length=4, choices=Analyse.ORDER_CHOICES)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
