from rest_framework import serializers
from courses.models import OrderDetail, Order


class OrderSerializer(serializers.ModelSerializer):
    order_details = serializers.SerializerMethodField(method_name='get_order_details')

    def get_order_details(self, obj):
        order_details = [
            {'id': detail.id, 'course': detail.course.title} for detail in obj.order_details.all()
        ]
        return order_details


    class Meta:
        model = Order
        fields = ('id', 'is_paid', 'created', 'payment_date', 'order_details')


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ('course',)
