from django.db import models

# Create your models here.
class File(models.Model):
    title = models.CharField(max_length=40)
    file = models.FileField(upload_to='files')
 
