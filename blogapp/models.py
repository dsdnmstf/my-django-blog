from django.db import models

# Create your models here.

class Blog(models.Model):
    STATUS_CHOICES = [
        ("DR", "Draft"),
        ("Pb", "Published"),
    ]
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True,max_length=200)
    image = models.ImageField(blank=True, null=True, upload_to="media/")
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    status = models.CharField( max_length=2, choices=STATUS_CHOICES, default="Draft")
    
