from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	preview_image = models.FilePathField(path="/img")
	reference_link = models.URLField(max_length=250)
