from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView 


from .serializer import ElectionSerializer, ElectorateSerializer, ContestantSerializer,VoterSerializer
from .models import Election, Contestant
from School.models import Electorate
from Voters.models import Voter 



class createElectorateApi(ListCreateAPIView):
    queryset = Electorate.objects.all()
    serializer_class = ElectorateSerializer
    permission_classes = [permissions.IsAdminUser]
    
# class listElectorateApi(ListAPIView):
#     queryset = Electorate.objects.all()
#     serializer_class = ElectorateSerializer
#     permission_classes = [permissions.IsAdminUser] 


class ElectionApi(APIView):
    serializer_class = ElectorateSerializer

    def get(self, request): 
        detail = [ {"name": detail.electorateName,"detail": detail.electorateEmail ,'id':detail.electorateId , 'desctiption':detail.electorateApproved }  
        for detail in Electorate.objects.all().order_by('-id')] 
        return Response(detail) 
  
    def post(self, request): 
  
        serializer = ReactSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True): 
            serializer.save() 
            return  Response(serializer.data) 

 





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
    permission_classes = [permissions.IsAdminUser]


# class listContestentApi(ListAPIView):
#     queryset = Contestant.objects.all().filter(electionName=963297842)
#     serializer_class = ContestantSerializer
#     permission_classes = [permissions.IsAdminUser]

@api_view(['GET'])
def listContestentApi(request,pk):
	tasks = Contestant.objects.all().filter(electionName=pk)
	serializer = ContestantSerializer(tasks, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def contestentDetail(request, pk):
	tasks = Contestant.objects.get(contestantName=pk)
	serializer = ContestantSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['GET', 'PUT'])
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

@api_view(['GET', 'PUT'])
def voterUpdate(request, pk):
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
            return Response ('Successful Updated')
            
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
        
    
# @api_view(['GET', 'DELETE'])
# def Election_Details(request,pk):
    
#     try:
#         contestants=Contestant.objects.get(electionName=pk)
#     except:
#         return Response ('Not Found')

#     if request.method == 'GET':

#         serializer = Election_Details_Serializer(instance=contestants)
#         return Response(serializer.data)
        
    


