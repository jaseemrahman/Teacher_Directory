from django.db import models

# Create your models here.
class BulkUpload(models.Model):
  date_uploaded = models.DateTimeField(auto_now=True)
  csv_file = models.FileField(upload_to='uploads')