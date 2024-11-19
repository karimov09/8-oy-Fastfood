from django.urls import path
from .views import CategoryAPIView, ProductAPIView, OrderAPIView

urlpatterns = [
    path('categories/', CategoryAPIView.as_view(), name='categories'),
    path('products/', ProductAPIView.as_view(), name='products'),
    path('orders/', OrderAPIView.as_view(), name='orders'),
]
