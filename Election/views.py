from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.core.mail import send_mail
from evotee.settings import EMAIL_HOST

from .serializer import ElectionSerializer, ElectorateSerializer, ContestantSerializer,VoterSerializer
from .models import Election, Contestant
from School.models import Electorate
from Voters.models import Voter 



class createElectorateApi(ListCreateAPIView):
    queryset = Electorate.objects.all()
    serializer_class = ElectorateSerializer
    permission_classes = [permissions.IsAdminUser]
    
class listElectorateApi(ListAPIView):
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

@api_view(['GET', 'PUT'])
def electorateUpdate(request, pk):
    try:
        model=Electorate.objects.get(electorateId = pk)
    except:
        return Response ('Not Found')
    
    if request.method == 'GET':

        serializer = ElectorateSerializer(instance=model)
        return Response(serializer.data)  
        
    if request.method == 'PUT':
        
        serializer = ElectorateSerializer(model, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ('Successful Updated')
            
        else:
            return Response ('Failed')

#  delete electorates on the bases electorateId
            
@api_view(['GET', 'DELETE'])
def electorateDelete(request, pk):
    try:
        model=Electorate.objects.get(electorateId= pk)
    except:
        return Response ('Not Found')
    
    if request.method == 'GET':

        serializer = ElectorateSerializer(instance=model)
        return Response(serializer.data)  
        
            
    if request.method == 'DELETE':
        model.delete()
        return Response ('Deleted')            





class ContestantApi(ListCreateAPIView):
    queryset = Contestant.objects.all()
    serializer_class = ContestantSerializer
    permission_classes = [permissions.AllowAny]


class listContestentApi(ListAPIView):
    queryset = Contestant.objects.all()
    serializer_class = ContestantSerializer
    permission_classes = [permissions.IsAdminUser]


@api_view(['GET'])
def contestentDetail(request, pk):
	tasks = Contestant.objects.get(contestantId=pk)
	serializer = ContestantSerializer(tasks, many=False)
	return Response(serializer.data)


@permission_classes([permissions.AllowAny])
@api_view(['GET','PUT'])
def contestantUpdate(request, pk):
    try:
        model=Contestant.objects.get(contestantId = pk)
    except:
        return Response ('Not Found')
    
    if request.method == 'GET':

        serializer = ContestantSerializer(instance=model)
        return Response(serializer.data)  
        
    if request.method == 'PUT':
        
        serializer = ContestantSerializer(model, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ('Successful Updated')
            
        else:
            return Response ('Failed')


            
@api_view(['GET', 'DELETE'])
def ContestantDelete(request, pk):
    try:
        model=Contestant.objects.get(contestantId= pk)
    except:
        return Response ('Not Found')
    
    if request.method == 'GET':

        serializer = ContestantSerializer(instance=model)
        return Response(serializer.data)  
        
            
    if request.method == 'DELETE':
        model.delete()
        return Response ('Deleted')            


@api_view(['POST','GET'])
def VotersApi(request):
    if request.method=='POST':
        model = Voter()
        serializer = VoterSerializer(instance = model,data=request.data)
        if serializer.is_valid():
            serializer.save()
            #TODO let it work with a try method
            send_mail('EVOTEE','Dear ' + str(request.data['firstName'])+' Welcome to the best voting System.', EMAIL_HOST,[request.data['email']] )
            #return Response('Something went wrong')
        return Response(serializer.data)

    if request.method == 'GET':
        model = Voter.objects.all()
        serializer = VoterSerializer(instance=model, many=True)
        return Response(serializer.data)

    

    
    
    

class listVoterApi(ListAPIView):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer
    permission_classes = [permissions.IsAdminUser]
    




@api_view(['GET'])
def voterDetail(request, pk):
	tasks = Voter.objects.get(idNumber=pk)
	serializer = VoterSerializer(tasks, many=False)
	return Response(serializer.data)

@api_view(['GET','PUT'])
def voterUpdate(request, pk):
    error = []
    try:
        model=Voter.objects.get(idNumber= pk)
    except:
        return Response ('Not Found')
    
    if request.method == 'GET':

        serializer = VoterSerializer(instance=model)
        return Response(serializer.data)  
        
    if request.method == 'PUT':
        
        serializer = VoterSerializer(model, request.data)
        if serializer.is_valid():
            serializer.save()
            try:
                send_mail('EVOTEE','Dear '+ str(model.firstName) + ' your detail has been updated if you did not request for an update contact us support@evotee.com '+ ' ','themaestrostech.inc@gmail.com', [model.email], fail_silently=False)
            except:
                error = 'but mailing was not successful, try again'
            return Response (' Successful Updated '+ str(error))
            
        else:
            return Response ('Failed')
            
@api_view(['GET', 'DELETE'])
def VoterDelete(request, pk):
    try:
        model=Voter.objects.get(idNumber= pk)
    except:
        return Response ('Not Found')
    
    if request.method == 'GET':

        serializer = VoterSerializer(instance=model)
        return Response(serializer.data)  
        
            
    if request.method == 'DELETE':
        model.delete()
        return Response ('Deleted')            

    
class createElectionApi(ListCreateAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
    permission_classes = [permissions.IsAdminUser]
class listElectionApi(ListAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionSerializer
    permission_classes=[permissions.AllowAny]

#get-detail
@api_view(['GET'])
def electionDetail(request, pk):
	election = Election.objects.get(electionId=pk)
	serializer = ElectionSerializer(election, many=False)
	return Response(serializer.data)

#update
@api_view(['GET', 'PUT'])
def electionUpdate(request, pk):
    try:
        model=Election.objects.get(electionId = pk)
    except:
        return Response ('Not Found')
    
    if request.method == 'GET':

        serializer = ElectionSerializer(instance=model)
        return Response(serializer.data)  
        
    if request.method == 'PUT':
        
        serializer = ElectionSerializer(model, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ('Successful Updated')
            
        else:
            return Response ('Failed')

@api_view(['GET', 'DELETE'])
def ElectionDelete(request, pk):
    try:
        model=Election.objects.get(electionId= pk)
    except:
        return Response ('Not Found')
    
    if request.method == 'GET':

        serializer = ElectionSerializer(instance=model)
        return Response(serializer.data)  
        
            
    if request.method == 'DELETE':
        model.delete()
        return Response ('Deleted')    
        
    