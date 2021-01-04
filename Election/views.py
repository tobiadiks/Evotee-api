from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

# getting details of each electorates on the bases electorateId

@api_view(['GET'])
def electorateDetail(request, pk):
	tasks = Electorate.objects.get(electorateId=pk)
	serializer = ElectorateSerializer(tasks, many=False)
	return Response(serializer.data)

#  update of each electorates on the bases electorateId

@api_view(['POST'])
def electorateUpdate(request, pk):
	task = Electorate.objects.get(electorateId=pk)
	serializer = ElectorateSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

#  delete electorates on the bases electorateId
@api_view(['DELETE'])
def electorateDelete(request, pk):
    task = Electorate.objects.get(electorateId=pk)

    task.delete()

    return Response('Contestent succsesfully delete!')





class ContestantApi(ListCreateAPIView):
    queryset = Contestant.objects.all()
    serializer_class = ContestantSerializer
    permission_classes = [permissions.IsAdminUser]


class listContestentApi(ListAPIView):
    queryset = Contestant.objects.all()
    serializer_class = ContestantSerializer
    permission_classes = [permissions.IsAdminUser]


@api_view(['GET'])
def contestentDetail(request, pk):
	tasks = Contestant.objects.get(contestantName=pk)
	serializer = ContestantSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def contestentUpdate(request, pk):
	task = Contestant.objects.get(contestantName=pk)
	serializer = ContestantSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def ContestentDelete(request, pk):
    task = Contestant.objects.get(idNumber=pk)

    task.delete()

    return Response('Contestent succsesfully delete!')



class VotersApi(ListCreateAPIView):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer
    permission_classes = [permissions.IsAdminUser]

class listVoterApi(ListAPIView):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer
    permission_classes = [permissions.IsAdminUser]




@api_view(['GET'])
def voterDetail(request, pk):
	tasks = Voter.objects.get(idNumber=pk)
	serializer = VoterSerializer(tasks, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def VoterUpdate(request, pk):
	task = Election.objects.get(idNumber=pk)
	serializer = VoterSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def VoterDelete(request, pk):
    task = Voter.objects.get(idNumber=pk)

    task.delete()

    return Response('Voter succsesfully delete!')


    
class listElectionApi(ListAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
    permission_classes = [permissions.AllowAny]



@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Election.objects.get(electionId=pk)
	serializer = ElectionSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def ElectioUpdate(request, pk):
	task = Election.objects.get(electionId=pk)
	serializer = ElectionSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)



@api_view(['DELETE'])
def ElectionDelete(request, pk):
    task = Election.objects.get(electionId=pk)

    task.delete()

    return Response('Election succsesfully delete!')
 
    #TODO:i will be making the update view, it required a lookup field 27/12/2020