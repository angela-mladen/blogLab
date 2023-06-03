from django.contrib import admin
from blogpost.models import BlogUser,BlocksUser,BlogPost,Comment

# Register your models here.

class BlogUserAdmin(admin.ModelAdmin):
    list_display = ("name",)

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False
    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title","user",)
    list_filter = ("dateCreated",)
    exclude = ("user",)

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        if (obj and obj.user.user == request.user) or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if(obj and obj.user.user == request.user) or request.user.is_superuser:
            return True
        return False

    def save_model(self, request, obj, form, change):
        if obj:
            obj.author=BlogUser.objects.get(user=request.user)
            super().save_model(request, obj, form, change)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("content","dateCreated",)
    exclude = ("user",)

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        if (obj and obj.user.user == request.user) or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if (obj and (obj.user.user == request.user or obj.post.user == request.user)) or request.user.is_superuser:
            return True
        return False

    def save_model(self, request, obj, form, change):
        if obj:
            obj.user = BlogUser.objects.get(user=request.user)
            super().save_model(request, obj, form, change)

class BlockUserAdmin(admin.ModelAdmin):
    list_display = ("blockedUser",)
    exclude = ("blockerUser",)

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.blockerUser.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and request.user == obj.blockerUser.user:
            return True
        return False

    def save_model(self, request, obj, form, change):
        if obj:
            obj.blockerUser = BlogUser.objects.get(user=request.user)
            super().save_model(request, obj, form, change)


admin.site.register(BlogUser,BlogUserAdmin)
admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(BlocksUser,BlockUserAdmin)