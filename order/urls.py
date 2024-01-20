from django.urls import path
from . import views
from order.views.CartListCreateView import CartListCreateView
from order.views.CartDetailView import CartDetailView


urlpatterns = [
    path('carts/', CartListCreateView.as_view(), name='cart-list-create'),
    path('carts/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
]