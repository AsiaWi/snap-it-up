from rest_framework import serializers
from .models import Offer
from django.contrib.humanize.templatetags.humanize import naturaltime

class OfferSerializer(serializers.ModelSerializer):
    buyer = serializers.ReadOnlyField(source='buyer.username')
    seller = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    created_by_profile_user = serializers.ReadOnlyField(source="buyer.profile.id")
    profile_image = serializers.ReadOnlyField(source="buyer.profile.profile_image.url")

    def get_seller(self,obj):
        return obj.advert.owner.username

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return naturaltime(obj.created_at)
        
    class Meta:
        model = Offer
        fields = '__all__'