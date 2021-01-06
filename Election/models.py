from django.db import models
from django.utils.timezone import now
from School.models import Electorate

import random
def generator():
		i=random.randint(100000000,999999999)
		return i


class Election(models.Model):
	electionName=models.CharField(max_length=200)
	electionId=models.IntegerField(primary_key = True, unique=True,default=generator)
	organizer=models.ForeignKey(Electorate, on_delete=models.CASCADE)
	is_active=models.BooleanField(default=False)
	startDate = models.DateField(default=now)
	endDate = models.DateField(default= now)
	
	
	def __str__(self):
		return str(self.electionName)
		


class Contestant(models.Model):
	contestantName=models.CharField(max_length=64,  null=False)


	position=models.CharField(max_length=40, default='')
	votes=models.IntegerField(default=0)
	electionName=models.ForeignKey(Election, on_delete=models.CASCADE)
	is_active=models.BooleanField(default=False)
	contestantId=models.IntegerField(primary_key=True , default = generator)
	
	def __str__(self):
		return self.contestantName
	

# Create your models here.
