from django.db import models
from django.core.validators import RegexValidator

class Submission(models.Model):
  email = models.EmailField()
  phone = models.CharField(blank=True, null=True, max_length=15)
  name = models.CharField(max_length=50)
  name_proposal = models.CharField(max_length=50)

  def __unicode__(self):
    return self.name

