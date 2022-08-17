from rest_framework import serializers
from .models import *

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields ='__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    store = StoreSerializer()
    products = OrderItemSerializer(many=True)
    
    class Meta:
        model = Order
        fields = ('id', 'user', 'products', 'order_date', 'order_state', 'store')

    def create(self, validated_data):
        product = validated_data.pop('products')
        sto = validated_data.pop('store')
        if sto:
            store = Store.objects.get_or_create(**sto)[0]
            validated_data['store'] = store
        order= Order.objects.create(**validated_data)
        for item in product:
            order.products.create(**item)
        return order

    def update(self, store, validated_data):
        store.user = validated_data.get('user', store.user)
        store.order_state = validated_data.get('order_state', store.order_state)
        store.save()
        return store
