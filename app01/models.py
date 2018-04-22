from django.db import models


class Passenger(models.Model):
    name = models.CharField(max_length=32)
    sex = models.CharField(max_length=32)
    survived = models.BooleanField()
    age = models.FloatField()
    ticket_class = models.PositiveSmallIntegerField()
    embarked = models.CharField(max_length=32)


class Department(models.Model):
    label = models.CharField(max_length=32)

class Employee(models.Model):
    name = models.CharField(max_length=32)
    dep = models.ForeignKey(to=Department,null=True)


