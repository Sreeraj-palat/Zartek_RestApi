from users.models import UserLiked

def count_for_each(id, status):
    return UserLiked.objects.filter(postId_id = id, like_status = status).count()
   