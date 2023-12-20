from .models import Rating
from rest_framework import serializers
from django.db import IntegrityError




class RatingSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    rated_user_name = serializers.ReadOnlyField(source='rated_user.username')
    
    # def get_is_owner(self, obj):
    #     request = self.context['request']
    #     return request.user == obj.owner

    class Meta:
        model = Rating
        fields = '__all__'

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})