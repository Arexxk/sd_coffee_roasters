from django.db import models

# Create your models here.
class User(models.Model):
	USER_TYPES = ((0,"admin"),(1,"business"),(2,"normal"))
	user_type = models.CharField(max_length=2, choices=USER_TYPES)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
