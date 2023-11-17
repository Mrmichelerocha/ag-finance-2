from rest_framework import serializers
from .models import Analyse, Buy, Sell, Wallet, Transaction

class AnalyseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analyse
        fields = '__all__'

class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Buy
        fields = '__all__'

class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = '__all__'

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
