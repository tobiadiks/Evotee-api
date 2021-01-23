from django.db import models
import random

def generator():
		i=random.randint(100000000,999999999)
		return i

class Electorate(models.Model):
	electorateName = models.CharField(max_length=200, unique=True)
	electorateEmail = models.EmailField(max_length=255, unique=True)
	electorateId=models.IntegerField(primary_key = True, unique=True,default=generator)
	electorateApproved = models.BooleanField(default=False)
	
	def __str__(self):
		return (self.electorateName)

