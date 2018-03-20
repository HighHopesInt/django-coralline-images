from django.contrib import admin
from coralline_userimages.models import UserImage


class UserImageAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'image_id')


admin.site.register(UserImage, UserImageAdmin)
