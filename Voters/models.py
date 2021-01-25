from django.db import models
from Election.models import Election



import random
def generator():
		i=random.randint(100000000,999999999)
		return i

gender_choices=(
    ('Male' , 'Male'),
    ( 'Female' , 'Female'),
    ( 'Not_Defined' , 'Not_Defined'),
)




class Voter(models.Model):
    firstName = models.CharField(max_length = 40)
    lastName = models.CharField(max_length = 40)
    Gender = models.CharField(max_length=12, choices=gender_choices , default='1')
    email = models.EmailField(default = "@")
    idNumber = models.IntegerField(primary_key = True)
    voterId = models.IntegerField(default=generator)
    #TODO Change idNumber to suit countries (NIN or CNIC)
    fatherName = models.CharField(max_length = 40)
    motherName = models.CharField(max_length = 40)
    qualifiedElection = models.ManyToManyField(Election)
    active = models.BooleanField(default=True)
    voted = models.BooleanField(default=False)
    id=models.IntegerField(
default=idNumber)


    def __str__(self):
        return str(self.idNumber) #TODO Change idNumber to suit countries (NIN or CNIC)

# Create your models here.
