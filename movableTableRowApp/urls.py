from django.urls import path
from .views import *

urlpatterns = [
    path('', mainView, name='mainView'),
    path('table/', mainTable, name='mainTable'),
    path('savePositions/', savePositions, name='savePositions'),
]
