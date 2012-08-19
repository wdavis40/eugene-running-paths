from django.db import models

# Create your models here.

class Path(models.Model):
  name = models.CharField(max_length=30)
  city = models.CharField(max_length=30)
  state_province = models.CharField(max_length=30)

  def __unicode__(self):
    return self.name

  class Meta:
    # This can be changed to affect the default order
    ordering = ['id']
