from rest_framework import serializers
from django.contrib.auth.models import User

from master.models import Image, Post
from users.models import UserLiked
from utils.total_likes_dislikes import count_for_each
from utils.get_tags import tag_list

class PostSerializer(serializers.Serializer):
    class meta:
        model= Post 
        exclude = ('updated_at', )

    def to_representation(self, instance):

        repressentation = super().to_representation(instance)
        repressentation['id'] = instance.id
        repressentation['caption'] = instance.name        
        repressentation['description'] = instance.description     
        repressentation['status'] = ""
        repressentation['likes'] = count_for_each(instance.id, True)
        repressentation['dislikes'] = count_for_each(instance.id, False)
        repressentation['tags'] = tag_list(instance)
        repressentation['created_at'] = instance.created_at.strftime("%m/%d/%Y, %H:%M")
        images = Image.objects.filter(post = instance.id)
        repressentation['images'] = [str(image.image.url) for image in images]
        return repressentation



class PostLikeSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    status = serializers.BooleanField()
    
    def validate(self, attrs):
        if not Post.objects.filter(id = attrs['post_id']):
            raise serializers.ValidationError("The post you are trying to like does not exist")
        return super().validate(attrs)

class InteractedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLiked
        fields = ('user',)

    def to_representation(self, instance):
        representation =  super().to_representation(instance)
        representation['names']= instance.user.username
        representation.pop('user')
        return representation