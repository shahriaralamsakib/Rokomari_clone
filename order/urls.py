from django.urls import path
from order.views.CartListCreate import CartListCreateView
from order.views.CartDetail import CartDetailView

urlpatterns = [

    path('carts/', CartListCreateView.as_view(), name='cart-list-create'),
    path('carts/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),


]