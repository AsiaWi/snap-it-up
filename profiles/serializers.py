from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    '''
    Profile model Serializer, all fields serialized
    owner is read only, is_owner returns true or false -
    if the requesting user is/is not a profile owner
    '''
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = '__all__'