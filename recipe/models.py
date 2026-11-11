from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    description = models.TextField(blank=True, default="")
    
    image = models.ImageField(upload_to="images/uploaded/", default=None, null=True, blank=True)

    detail_main = ImageSpecField(
        source="image",
        processors=[ResizeToFill(640, 480)],
        format="jpeg",
        options={"quality": 80}
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title