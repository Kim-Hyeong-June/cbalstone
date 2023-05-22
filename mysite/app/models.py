from django.db import models

from users.models import User as user_model


class Post(models.Model):
    author = models.ForeignKey(
                user_model, 
                null=True, 
                on_delete=models.CASCADE, 
                related_name='posts'
            )
    image = models.ImageField(blank=True, upload_to='post_images')
    

    
    location = models.CharField(blank=True, max_length=255)
    career = models.CharField(blank=True, max_length=255)
    salary = models.CharField(blank=True, max_length=255)
    company = models.CharField(blank=True, max_length=255)
    title = models.CharField(blank=True, max_length=255)
    
    start_at = models.CharField(blank=True, max_length=255)
    end_at = models.CharField(blank=True, max_length=255)

    image_likes = models.ManyToManyField(user_model, related_name='liked_posts')

    def __str__(self):
        return f"{self.company}"

    
class Apply(models.Model):
    author = models.ForeignKey(
            user_model, 
            null=True, 
            on_delete=models.CASCADE, 
            related_name='applies'
        )
    post = models.ForeignKey(
            Post, 
            null=True, 
            on_delete=models.CASCADE, 
            related_name='applies'
        )
    
    career = models.CharField(blank=True, max_length=255)
    salary = models.CharField(blank=True, max_length=255)
    contents = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.author}"
    