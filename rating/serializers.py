from .models import Rating
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime


class RatingSerializer(serializers.ModelSerializer):
    '''
    Rating model serializer, all fields serialized.
    Owner set to read only.
    Create function checks if owner wants to rate own profile-
    -if so- error is thrown.
    If not= rating instance is created
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    
    def create(self, validated_data):
        rated_user = validated_data['rated_user']
        owner = self.context['request'].user
        if rated_user == owner:
            raise serializers.ValidationError({'detail': 'You cannot rate your own profile'})

        rating_instance = Rating.objects.create(
            owner=owner,
            rated_user=rated_user,
            rating=validated_data['rating'],
            feedback=validated_data.get('feedback', '')
        )
        return rating_instance
    
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.created_at)
        
    class Meta:
        model = Rating
        fields = '__all__'
