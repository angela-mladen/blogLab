
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BlogUser(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title=models.CharField(max_length=50)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE,null=True)
    contents=models.TextField()
    files=models.FileField(upload_to="filesUploaded/")
    dateCreated=models.DateField()
    dateModified=models.DateField()

    def __str__(self):
        return f"{self.title} - {self.user.name}"



class Comment(models.Model):
    content=models.TextField()
    dateCreated=models.DateField()
    post=models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    user=models.ForeignKey(BlogUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name

class BlocksUser(models.Model):
    blockerUser=models.ForeignKey(BlogUser,on_delete=models.CASCADE,related_name="blogUser_blocker")
    blockedUser=models.ForeignKey(BlogUser,on_delete=models.CASCADE,related_name="blogUser_blocked")

    def __str__(self):
        return f"{self.blockerUser.user} blocked {self.blockedUser.user}"





