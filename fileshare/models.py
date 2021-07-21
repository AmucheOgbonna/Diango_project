from django.db import models

# Create your models here.
class photo(models.Model):
    file = models.FileField(upload_to='file')