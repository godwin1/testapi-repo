from django.db import models

class Contacts(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(max_length=1000);
	datePosted = models.DateField(auto_now_add=True)
	author = models.CharField(max_length=30)



