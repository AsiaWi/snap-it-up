from rest_framework import serializers
from .models import Profile
from django.contrib.humanize.templatetags.humanize import naturaltime


class ProfileSerializer(serializers.ModelSerializer):
    '''
    Profile model Serializer, all fields serialized
    owner is read only, is_owner returns true or false -
    to check if the requesting user is/is not a profile owner
    '''
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    advert_count = serializers.ReadOnlyField()
    rating_count = serializers.ReadOnlyField()
    average_rating = serializers.SerializerMethodField()
    
    def get_average_rating(self, obj):
        return round(obj.calculate_average_rating(),2)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    class Meta:
        model = Profile
        fields = '__all__'