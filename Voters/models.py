from django.db import models
from Election.models import Election

class Voter(models.Model):
    firstName = models.CharField(max_length = 40)
    lastName = models.CharField(max_length = 40)
    Gender = models.CharField(max_length = 1)
    idNumber = models.IntegerField(primary_key = True)
    #TODO Chaange idNumber to suit countries (NIN or CNIC)
    fatherName = models.CharField(max_length = 40)
    motherName = models.CharField(max_length = 40)
    qualifiedElection = models.ManyToManyField(Election)
    active = models.BooleanField(default=True)
    voted = models.BooleanField(default=False)


    def __str__(self):
        return str(self.idNumber) #TODO Chaange idNumber to suit countries (NIN or CNIC)

# Create your models here.
