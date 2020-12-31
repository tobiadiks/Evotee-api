from django.urls import path
from .views import ElectionApi,ElectorateApi, ContestantApi, UpdateElection

urlpatterns = [
    path('api/election', ElectionApi.as_view()),
    path('api/electorate',ElectorateApi.as_view()),
    path('api/contestant', ContestantApi.as_view()),
    path('api/update/election', UpdateElection.as_view())
]
