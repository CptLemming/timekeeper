from django.db import models
from django.utils import timezone


class Customer(models.Model):
    name = models.CharField(max_length=128)
    tel = models.CharField(max_length=24)
    mobile = models.CharField(max_length=24)
    email = models.CharField(max_length=128)
    def __unicode__(self):
        return self.name


class CustomerProject(models.Model):
    customer = models.ForeignKey(Customer)
    name = models.CharField(max_length=256)
    def __unicode__(self):
        return self.name


class CustomerProjectJob(models.Model):
    project = models.ForeignKey(CustomerProject)
    name = models.CharField(max_length=256)
    start_date = models.DateTimeField('start date')
    status = models.CharField(max_length=32)
    def __unicode__(self):
        return self.name