from rest_framework import serializers
from .models import Election, Contestant
from School.models import Electorate
from Voters.models import Voter

class ElectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = ('electionName','electionId','organizer','is_active')

class ElectorateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Electorate
        fields = ('electorateName', 'electorateEmail', 'electorateId','electorateApproved')

class ContestantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contestant
        fields = ('contestantName','position','votes','electionName','is_active','contestantId')

class VoterSerializer(serializers
.ModelSerializer):
    class Meta:
        model = Voter
        fields = '__all__'
