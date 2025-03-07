from django.db import models

# Create your models here.
class Products(models.Model):
	title = models.CharField(max_length=255);
	image = models.CharField(max_length=255);
	likes = models.PositiveBigIntegerField(default=0);

class User(models.Model):
	pass