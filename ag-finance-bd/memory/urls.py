from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BuyViewSet, SellViewSet, WalletViewSet, TransactionViewSet, AnalyseViewSet

router = DefaultRouter()
router.register('buys', BuyViewSet, basename='buy')
router.register('sells', SellViewSet, basename='sell')
router.register('wallet', WalletViewSet, basename='wallet')
router.register('transactions', TransactionViewSet, basename='transaction')
router.register('analyse', AnalyseViewSet, basename='analyse')

urlpatterns = [
    path('', include(router.urls)),
    path('index/', views.index, name='index'),
    path('update_status/', views.update_status, name='update_status'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
