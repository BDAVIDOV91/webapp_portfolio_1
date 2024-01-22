from django.db import models

# Create your models here.
class Project(models.Model):
    app_label = 'webapp_portfolio'
    name = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField()
    technology = models.CharField(max_length=255)
    accomplishments = models.TextField()
 