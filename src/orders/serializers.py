from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields=["orders","products","quantity","unit_price","discount_amount"]


class OrderSerializer(serializers.ModelSerializer):
    order_items=OrderItemSerializer(many=True)
    class Meta:
        model=Order
        fields=['customer','discount_amount','payment_amount','order_items']
