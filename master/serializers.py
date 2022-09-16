from rest_framework import serializers



class PostSerializer(serializers.Serializer):
    def validate(self, attrs):
        return super().validate(attrs)