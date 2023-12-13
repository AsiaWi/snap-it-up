from rest_framework import serializers
from .models import Advert
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class AdvertSerializer(TaggitSerializer, serializers.ModelSerializer):
    '''
    Advert model Serializer, all fields serialized
    profile_owner is read only, is_owner returns true or false -
    if the requesting user is/is not a profile owner
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    tags = TagListSerializerField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    page_views = serializers.SerializerMethodField()
    
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def validate(self, data):
        advert_title = data.get('advert_title')
        tags = data.get('tags')
        if not advert_title and not tags:
            raise ValidationError('At least one of the fields: advert title or tags must be provided')
        return data

    def get_page_views(self, obj):
        try:
            return obj.hit_count.hits
        except:
            pass
    # this function fully copied from CI walkthrough
    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

  

    class Meta:
        model = Advert
        fields = '__all__'
