from rest_framework import serializers
from .models import Reply
from django.contrib.humanize.templatetags.humanize import naturaltime


class ReplySerializer(serializers.ModelSerializer):
    '''
    Reply model serializer, reply content with elapsed time shown
    (naturaltime implementation)
    Profile of the reply owner
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    created_by_profile_user = serializers.ReadOnlyField(
                              source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(
                    source="owner.profile.profile_image.url")

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.created_at)

    class Meta:
        model = Reply
        fields = '__all__'


class ReplyDetailsSerializer(ReplySerializer):
    '''
    Serializer for the reply shown in detail view
    Question releted to the reply set as read only
    '''
    question = serializers.ReadOnlyField(source='question.id')
