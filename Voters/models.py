from django.db import models
from Election.models import Election




gender_choices=(
    ('Male' , 'Male'),
    ( 'Femaile' , 'Female'),
    ( 'Not_Defined' , 'Not_Defined'),
)




class Voter(models.Model):
    firstName = models.CharField(max_length = 40)
    lastName = models.CharField(max_length = 40)
    Gender = models.CharField(max_length=12, choices=gender_choices , default='1')
    idNumber = models.IntegerField(primary_key = True)
    #TODO Chaange idNumber to suit countries (NIN or CNIC)
    fatherName = models.CharField(max_length = 40)
    motherName = models.CharField(max_length = 40)
    qualifiedElection = models.ManyToManyField(Election)
    active = models.BooleanField(default=True)
    voted = models.BooleanField(default=False)
    id=models.IntegerField(
default=0)


    def __str__(self):
        return str(self.idNumber) #TODO Chaange idNumber to suit countries (NIN or CNIC)

# Create your models here.
