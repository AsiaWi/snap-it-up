# from rest_framework import serializers
# from .models import Advert
# from taggit.serializers import (TagListSerializerField,
#                                 TaggitSerializer)


# class AdvertSerializer(TaggitSerializer, serializers.ModelSerializer):
#     '''
#     Advert model Serializer, all fields serialized
#     profile_owner is read only, is_owner returns true or false -
#     if the requesting user is/is not a profile owner
#     '''
#     advert_owner = serializers.ReadOnlyField(source="advert_owner.username")
#     is_owner = serializers.SerializerMethodField()
#     tags = TagListSerializerField()
#     profile_id = serializers.ReadOnlyField(source='advert_owner.profile.id')
#     profile_image = serializers.ReadOnlyField(source='advert_owner.profile.image.url')
    
#     # this function fully copied from CI walkthrough
#     def validate_image(self, value):
#         if value.size > 2 * 1024 * 1024:
#             raise serializers.ValidationError('Image size larger than 2MB!')
#         if value.image.height > 4096:
#             raise serializers.ValidationError(
#                 'Image height larger than 4096px!'
#             )
#         if value.image.width > 4096:
#             raise serializers.ValidationError(
#                 'Image width larger than 4096px!'
#             )
#         return value

#     def get_is_owner(self, obj):
#         request = self.context['request']
#         return request.user == obj.advert_owner

#     class Meta:
#         model = Advert
#         fields = '__all__'