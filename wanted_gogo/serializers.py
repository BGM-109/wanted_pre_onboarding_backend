from rest_framework import serializers
from .models import Funding

class FundingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Funding
        fields = ['id', 'title', 'description', 'author', 'target_price', 'session_price', 'end_date']