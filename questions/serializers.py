from rest_framework import serializers
from .models import Question
from django.contrib.humanize.templatetags.humanize import naturaltime
# from replies.serializers import ReplySerializer

class QuestionSerializer(serializers.ModelSerializer):
    '''
    Question model serializer, question content with elapsed time shown(naturaltime implementation)
    Profile of the question owner 
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    asked_by_profile_user = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.profile_image.url")

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.created_at)

    class Meta:
        model = Question
        fields = '__all__'


class QuestionDetailsSerializer(QuestionSerializer):
    '''
    Serializer for the question shown in detail view
    '''
    advert = serializers.ReadOnlyField(source='advert.id')
    # replies = ReplySerializer(many= True)

    class Meta:
        model = Question
        fields = '__all__'