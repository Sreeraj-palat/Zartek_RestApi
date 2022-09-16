from django.db import models
from django.contrib.auth.models import User

from master.models import Post

# Create your models here.
class UserLiked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_status = models.BooleanField(null=True, blank= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.postId.name if self.postId.name else None 