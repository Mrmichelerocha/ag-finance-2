from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Buy, Sell, Transaction, Wallet

@receiver(pre_save, sender=Buy)
def update_buy_status(sender, instance, **kwargs):
    if instance.status == 'off':
        Transaction.objects.create(symbol=instance.symbol, price=instance.price, order=instance.order, quantity=instance.quantity)
        update_wallet(instance.symbol, instance.quantity, 'buy')

@receiver(pre_save, sender=Sell)
def update_sell_status(sender, instance, **kwargs):
    if instance.status == 'off':
        Transaction.objects.create(symbol=instance.symbol, price=instance.price, order=instance.order, quantity=instance.quantity)
        update_wallet(instance.symbol, instance.quantity, 'sell')

def update_wallet(symbol, quantity, order):
    wallet, created = Wallet.objects.get_or_create(symbol=symbol, defaults={'quantity': 0})
    if order == 'buy':
        wallet.quantity += quantity
    else:
        wallet.quantity -= quantity
    if wallet.quantity == 0:
        wallet.delete()
    else:
        wallet.save()
