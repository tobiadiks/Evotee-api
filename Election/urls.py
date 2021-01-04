from django.urls import path
from .views import ElectionApi,ElectorateApi, ContestantApi, VotersApi, listElectionApi

urlpatterns = [
    path('api/create/election', ElectionApi.as_view()),
    path('api/create/electorate',ElectorateApi.as_view()),
    path('api/creatcreate/contestant', ContestantApi.as_view()),
    path('api/create/voters', VotersApi.as_view()),
    path('api/list/election', listElectionApi.as_view())
]
