from django.db import models

# Create your models here.

class Input(models.Model):
	document = models.FileField(upload_to='documents/')