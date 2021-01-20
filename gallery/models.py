from django.db import models
import datetime

class Gallery(models.Model):
    img_title = models.CharField(max_length=250)
    img_file = models.ImageField(upload_to="gallery")
    is_updated = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(default=datetime.date.today)
    updated_at = models.DateField(auto_now=False,null=True)
    deleted_at = models.DateField(auto_now=False,null=True)
