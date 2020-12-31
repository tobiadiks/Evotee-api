from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from .serializer import ElectionSerializer, ElectorateSerializer, ContestantSerializer
from .models import Election, Contestant
from School.models import Electorate

class ElectionApi(ListCreateAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer

class ElectorateApi(ListCreateAPIView):
    queryset = Electorate.objects.all()
    serializer_class = ElectorateSerializer

class ContestantApi(ListCreateAPIView):
    queryset = Contestant.objects.all()
    serializer_class = ContestantSerializer

class UpdateElection(UpdateAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
    #TODO:i will be making the update view, it required a lookup field 27/12/2020