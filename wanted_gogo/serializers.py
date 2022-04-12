from rest_framework import serializers
from .models import Funding

class FundingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Funding
        fields = ['id', 'title', 'description', 'author', 'target_price', 'session_price', 'end_date']
        extra_kwargs = {
            'target_price': {'read_only': True},
        }

class PutFundingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Funding
        fields = ['id', 'title', 'description', 'author', 'target_price', 'session_price', 'end_date']
        read_only_fields = ['target_price']