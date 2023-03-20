from rest_framework import serializers
from followers.models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = ['id', 'owner', 'created_at', 'followed', 'followed_name']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntergrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
