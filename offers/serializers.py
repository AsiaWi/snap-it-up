from rest_framework import serializers
from .models import Offer
from django.contrib.humanize.templatetags.humanize import naturaltime


class OfferSerializer(serializers.ModelSerializer):
    '''
    All Offer model fields serialized.
    Time for created and updated field displayed with the help
    of naturaltime.
    Profile ID and profile image - additional fields
    '''
    buyer = serializers.ReadOnlyField(source='buyer.username')
    seller = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    created_by_profile_user = serializers.ReadOnlyField(
                              source="buyer.profile.id")
    profile_image = serializers.ReadOnlyField(
                    source="buyer.profile.profile_image.url")

    def get_seller(self, obj):
        return obj.advert.owner.username

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.created_at)

    class Meta:
        model = Offer
        fields = '__all__'


class OfferListSerializer(OfferSerializer):
    '''
    OfferListSerializer with OfferSerializer passed in
    Overriden displayed serialized fields, excluded message
    field in list view to allow users privately share personal
    details once transaction is accepted
    '''
    class Meta:
        model = Offer
        exclude = ['message']
