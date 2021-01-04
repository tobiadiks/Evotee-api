from django.urls import path
from .views import ElectionApi,ElectorateApi,\
    ContestantApi, VotersApi, listElectionApi,listVoterApi,listContestentApi
from .import views
urlpatterns = [
    path('api/create/election', ElectionApi.as_view()),

    #Electorate  urls
    path('api/create/electorate',ElectorateApi.as_view()),

    path('api/electorate-detail/<str:pk>/', views.electorateDetail, name="electorate-detail"), # try http://localhost:8000/api/electorate-detail/988063249/
    path('api/electorate-update/<str:pk>/', views.electorateUpdate, name="electorate-update"), #try http://localhost:8000/api/electorate-update/988063249/
    path('api/delete-electorate/<str:pk>/', views.electorateDelete, name="delete-electorate"), # http://localhost:8000/api/delete-electorate/988063249/


    #contestent CRUD urls
    path('api/create/contestant', ContestantApi.as_view()),
    path('api/list/contestent', listContestentApi.as_view()),
    path('api/contestent-detail/<str:pk>/', views.contestentDetail, name="contestent-detail"),  # try http://localhost:8000/api/contestent-detail/Aqbar Jamiu/
    path('api/contestent-update/<str:pk>/', views.contestentUpdate, name="contestent-update"),
    path('api/delete-contestent/<str:pk>/', views.ContestentDelete, name="delete-contestent"),


    #Voter CRUD urls
    path('api/create/voters', VotersApi.as_view()),
    path('api/list/voters', listVoterApi.as_view()),
    path('api/voter-detail/<str:pk>/', views.voterDetail, name="task-detail"),
    path('api/voter-update/<str:pk>/', views.VoterUpdate, name="voter-update"),
    path('api/delete-voter/<str:pk>/', views.VoterDelete, name="delete-voter"),

    #Election CRUD urls
    path('api/list/election', listElectionApi.as_view()),
    path('api/voter-detail/<str:pk>/', views.taskDetail, name="task-detail"),
    path('api/task-update/<str:pk>/', views.ElectioUpdate, name="election-update"),
    path('api/delete-election/<str:pk>/', views.ElectionDelete, name="election-delete"),
]
