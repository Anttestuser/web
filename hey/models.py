from django.db import models


# Create your models here.
class UploadFiles(models.Model):
    name = models.CharField(max_length=50)
    file = models.ImageField(upload_to='uploads_model')
