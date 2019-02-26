from django.db import models

# Create your models here.

class InputImage(models.Model):
	image = models.FileField(upload_to='input/')