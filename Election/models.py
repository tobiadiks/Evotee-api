from django.db import models
from School.models import Electorate

import random
def generator():
		i=random.randint(100000000,999999999)
		return i


class Election(models.Model):
	electionName=models.CharField(max_length=200)
	electionId=models.IntegerField(unique=True,default=generator)
	organizer=models.ForeignKey(Electorate, on_delete=models.CASCADE)
	is_active=models.BooleanField(default=True)
	
	
	def __str__(self):
		return str(self.electionId)
		
		
class Contestant(models.Model):
	contestantName=models.CharField(max_length=30, default= '')
	position=models.CharField(max_length=40, default='')
	votes=models.IntegerField(default=0)
	electionName=models.ForeignKey(Election, on_delete=models.CASCADE)
	is_active=models.BooleanField(default=True)
	
	def __str__(self):
		return self.contestantName

class Voter(models.Model):
	electionVoted = models.ForeignKey(Election, on_delete=models.CASCADE)
	VoterId=models.IntegerField(default=generator)
	is_active=models.BooleanField(default=True)

	def __str__(self):
		return str(self.VoterId)
	

# Create your models here.
