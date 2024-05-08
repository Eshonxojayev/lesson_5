from rest_framework import serializers
from .models import Billing, Customer, Product

class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    billing = BillingSerializer(read_only=True)
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    # customer = CustomerSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'