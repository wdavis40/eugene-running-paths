from django.db import models

# Create your models here.

class Path(models.Model):
  name = models.CharField(max_length=30)
  city = models.ForeignKey('City')
  state_province = models.CharField(max_length=30)
  surface = models.ForeignKey('Surface', null=True)

  def __unicode__(self):
    return self.name

class City(models.Model):
  name = models.CharField(max_length=30)
  state = models.ForeignKey('State', null=True)

  def __unicode__(self):
    return self.name

class State(models.Model):
  name = models.CharField(max_length=30)

  def __unicode__(self):
     return self.name

class Surface(models.Model):
  name = models.CharField(max_length=30)

  def __unicode__(self):
     return self.name
