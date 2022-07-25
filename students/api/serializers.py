from rest_framework import serializers
from courses.models import OrderDetail, Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('is_paid', 'created', 'payment_date')

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ('course',)

class OrderDetailDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ('order', 'id')
