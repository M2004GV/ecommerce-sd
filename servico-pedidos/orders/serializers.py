from django.db import transaction
from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("id", "product_name", "quantity")

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("A quantidade deve ser pelo menos 1.")
        return value


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, required=False)

    class Meta:
        model = Order
        fields = ("id", "customer_name", "status", "created_at", "items")
        read_only_fields = ("created_at",)

    @transaction.atomic
    def create(self, validated_data):
        items_data = validated_data.pop("items", [])
        order = Order.objects.create(**validated_data)
        self._criar_itens(order, items_data)
        return order

    @transaction.atomic
    def update(self, instance, validated_data):
        items_data = validated_data.pop("items", None)

        for campo, valor in validated_data.items():
            setattr(instance, campo, valor)
        instance.save()

        if items_data is not None:
            instance.items.all().delete()
            self._criar_itens(instance, items_data)

        return instance

    @staticmethod
    def _criar_itens(order, items_data):
        OrderItem.objects.bulk_create([OrderItem(order=order, **item) for item in items_data])
