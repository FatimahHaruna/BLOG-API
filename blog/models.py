from django.db import models

# Create your models here.
class BlogPost(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.blog_title
    
