from django.db import models

class SchoolPage(models.Model):
    title = models.CharField(max_length=200)
    heading = models.CharField(max_length=200)
    description = models.TextField()
    hero_image = models.ImageField(upload_to='school_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    caption = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Gallery Images"
    
    def __str__(self):
        return self.title