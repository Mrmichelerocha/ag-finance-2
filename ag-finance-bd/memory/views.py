from django.shortcuts import render
from rest_framework.mixins import (
    CreateModelMixin, 
    ListModelMixin, 
    RetrieveModelMixin, 
    UpdateModelMixin, 
    DestroyModelMixin
)
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import GenericViewSet
from .models import Buy, Sell, Wallet, Transaction, Analyse
from .serializers import BuySerializer, SellSerializer, WalletSerializer, TransactionSerializer, AnalyseSerializer
    
def index(request):
    sell_items = Sell.objects.filter(status='on').order_by('-date')
    buy_items = Buy.objects.filter(status='on').order_by('-date')

    context = {
        'sell_items': sell_items,
        'buy_items': buy_items,
    }

    return render(request, 'index.html', context)

from django.http import JsonResponse

@api_view(['POST'])
def adicionar_algo(request):
    return Response({'success': True})

def update_status(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item_type = request.POST.get('item_type')

        # Verifique se o item_type é 'buy' ou 'sell' e atualize o status para 'off' no banco de dados
        if item_type == 'buy':
            Buy.objects.filter(id=item_id).update(status='off')
        elif item_type == 'sell':
            Sell.objects.filter(id=item_id).update(status='off')

        return JsonResponse({'message': 'Status atualizado com sucesso'})

    return JsonResponse({'message': 'Método não permitido'}, status=405)


class BuyViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Buy.objects.all()
    serializer_class = BuySerializer

class SellViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

class WalletViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class TransactionViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class AnalyseViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Analyse.objects.all()
    serializer_class = AnalyseSerializer
