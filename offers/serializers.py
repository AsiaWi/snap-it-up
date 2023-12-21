from rest_framework import serializers
from .models import Offer
from django.contrib.humanize.templatetags.humanize import naturaltime

class OfferSerializer(serializers.ModelSerializer):
    buyer = serializers.ReadOnlyField(source='buyer.username')
    seller = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    
    def get_seller(self,obj):
        return obj.advert.owner.username

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return naturaltime(obj.created_at)

    def create(self, validated_data):
        user = self.context['request'].user
        advert = validated_data.get('advert')

        if advert.owner == user:
            validated_data['seller'] = user
            return super().create(validated_data)

        validated_data['buyer'] = user
        return super().create(validated_data)
    class Meta:
        model = Offer
        fields = '__all__'