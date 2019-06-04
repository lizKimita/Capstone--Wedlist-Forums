from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length = 100)

    def save_status(self):
        self.save()

    def delete_status(self):
        self.delete()   


    def __str__(self):
        return self.status

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'images/', blank = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    bio = models.TextField(max_length = 100)
    status = models.ForeignKey(Status,on_delete = models.CASCADE,null = True)
    userId =models.IntegerField(default = 0)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()   

    def update_bio(self,bio):
        self.bio = bio
        self.save()

    @classmethod
    def find_user(cls, profile_id):
        profile = cls.objects.get(id=profile_id)
        return profile

    @classmethod
    def update_profile(cls,profile,update):
         updated = cls.objects.filter(Image_name=profile).update(name=update)
         return updated

    def __str__(self):
        return self.bio


class Posts(models.Model):
    title = models.CharField(max_length = 30)
    post_image = models.ImageField(upload_to = 'images/', blank=True)
    description = models.TextField(blank= True)
    profile = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    status = models.ForeignKey(Status, on_delete = models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    poster_id = models.IntegerField(default=0)


    def save_post(self):
        self.save()

    def delete_post(self):
        Posts.objects.filter().delete()
    
    @classmethod
    def get_posts(cls):
        posts = Posts.objects.all()
        return posts

    @classmethod
    def get_post(cls, post_id):
        single_post = cls.objects.get(id=post_id)
        return single_post

    @classmethod
    def search_by_title(cls,search_term):
        post = cls.objects.filter(title__icontains=search_term)
        return post

    class Meta:
        ordering = ['-id']