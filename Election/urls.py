from django.urls import path
from .views import *


urlpatterns = [
    #Electorate  urls
    path('api/create/electorate',createElectorateApi.as_view()),
    # path('api/list/electorate', listElectorateApi.as_view()),

    path('api/electorate-detail/<str:pk>/', electorateDetail, name="electorate-detail"), # try http://localhost:8000/api/electorate-detail/988063249/
    path('api/electorate-update/<str:pk>/', electorateUpdate, name="electorate-update"), #try http://localhost:8000/api/electorate-update/988063249/
    path('api/electorate-delete/<str:pk>/', electorateDelete, name="delete-electorate"), # http://localhost:8000/api/delete-electorate/988063249/


    #contestent CRUD urls
    path('api/create/contestant', ContestantApi.as_view()),
    path('api/list/contestant', listContestentApi.as_view()),
    path('api/contestant-detail/<str:pk>/', contestentDetail, name="contestant-detail"),  # try http://localhost:8000/api/contestent-detail/Aqbar Jamiu/
    path('api/contestant-update/<str:pk>/', contestantUpdate, name="contestant-update"),
    path('api/contestant-delete/<str:pk>/', ContestantDelete, name="delete-contestant"),


    #Voter CRUD urls
    path('api/create/voters', VotersApi.as_view()),
    path('api/list/voters', listVoterApi.as_view()),
    path('api/voter-detail/<str:pk>/', voterDetail, name="task-detail"),
    path('api/voter-update/<str:pk>/', voterUpdate, name="voter-update"),
    path('api/voter-delete/<str:pk>/', VoterDelete, name="delete-voter"),

    #Election CRUD urls
    path('api/create/election', createElectionApi.as_view()),
    path('api/list/election', listElectionApi.as_view()),
    path('api/election-detail/<str:pk>/', electionDetail, name="election-detail"),
    path('api/election-update/<str:pk>/', electionUpdate, name="election-update"),
    path('api/election-delete/<str:pk>/', ElectionDelete, name="election-delete"),
]
