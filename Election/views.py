from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework import permissions

from .serializer import ElectionSerializer, ElectorateSerializer, ContestantSerializer,VoterSerializer
from .models import Election, Contestant
from School.models import Electorate
from Voters.models import Voter 

class ElectionApi(ListCreateAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
    permission_classes = [permissions.IsAdminUser]

class ElectorateApi(ListCreateAPIView):
    queryset = Electorate.objects.all()
    serializer_class = ElectorateSerializer
    permission_classes = [permissions.IsAdminUser]

class ContestantApi(ListCreateAPIView):
    queryset = Contestant.objects.all()
    serializer_class = ContestantSerializer
    permission_classes = [permissions.IsAdminUser]

class VotersApi(ListCreateAPIView):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer
    permission_classes = [permissions.IsAdminUser]
    
class listElectionApi(ListAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
    permission_classes = [permissions.AllowAny]
 
    #TODO:i will be making the update view, it required a lookup field 27/12/2020