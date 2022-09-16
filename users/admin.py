from django.contrib import admin

from users.models import UserLiked

# Register your models here.
class UserLikedAdmin(admin.ModelAdmin):
    model= UserLiked
    list_display = (
        'postId',
        'user',
        'like_status'
    )

admin.site.register(UserLiked, UserLikedAdmin)